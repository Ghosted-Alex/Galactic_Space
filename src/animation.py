"""Module for Animations"""

import config
from . import assets
import time
import pygame

class ShootEffect:
    """Handles visual effects for weapon firing or energy discharge."""

    def __init__(self, x: float, y: float, duration: float = 0.2):
        self.x = x
        self.y = y
        self.duration = duration
        self.elapsed_time = 0.0
        self.active = True

    def update(self, dt: float):
        self.elapsed_time += dt
        if self.elapsed_time >= self.duration:
            self.active = False

    def draw(self, surface: pygame.Surface):
        if not self.active:
            return

        progress = self.elapsed_time / self.duration
        # Example flash effect: radius shrinks or grows as it fades out
        radius = int(15 * (1.0 - progress))
        alpha = int(255 * (1.0 - progress))

        if radius > 0:
            # Draw a quick expanding muzzle flash ring
            flash_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(flash_surf, (255, 255, 200, alpha), (radius, radius), radius)
            surface.blit(flash_surf, (int(self.x - radius), int(self.y - radius)))

class Tween:
    """Helper class for mathematical easing and value interpolation over time."""

    @staticmethod
    def lerp(start: float, end: float, progress: float) -> float:
        """Linear interpolation between start and end based on progress (0.0 to 1.0)."""
        return start + (end - start) * progress

    @staticmethod
    def ease_in_quad(progress: float) -> float:
        """Quadratic ease-in for accelerating charge-up effects."""
        return progress * progress


class ChargeAnimation:
    """Handles the visual math for the ship's pre-gameplay charge-up sequence."""

    def __init__(self, duration: float):
        self.duration = duration

    def get_progress(self, elapsed_time: float) -> float:
        """Returns a normalized progress value clamped between 0.0 and 1.0."""
        if self.duration <= 0:
            return 1.0
        return min(1.0, max(0.0, elapsed_time / self.duration))

    def get_radius(self, elapsed_time: float, min_r: int, max_r: int) -> int:
        progress = self.get_progress(elapsed_time)
        # Use ease-in squared for a satisfying acceleration curve
        eased = progress * progress
        return int(min_r + (max_r - min_r) * eased)


import pygame


class SpriteSheetAnimation:
    def __init__(self, sheet: pygame.Surface, frame_width: int, frame_height: int, duration: float,
                 scale_factor: int = 1, stride_x: int = None, max_frames: int = None):
        self.duration = duration
        self.frames = []

        if stride_x is None:
            stride_x = frame_width

        sheet_width, sheet_height = sheet.get_size()
        cols = max(1, sheet_width // stride_x)
        total_to_extract = max_frames if max_frames is not None else cols * (sheet_height // frame_height)

        print(
            f"DEBUG -> Sheet Size: {sheet_width}x{sheet_height} | Stride: {stride_x} | Target Frames: {total_to_extract}")

        for i in range(total_to_extract):
            col = i % cols
            row = i // cols

            x = col * stride_x
            y = row * frame_height

            # If our rect goes outside the sheet, clamp or skip gracefully so we don't crash or make tiny blocks
            if x >= sheet_width or y >= sheet_height:
                print(
                    f"WARNING: Frame {i} at ({x}, {y}) is outside sheet bounds ({sheet_width}x{sheet_height}). Stopping extraction.")
                break

            # Clamp width/height to available sheet space just in case
            w = min(frame_width, sheet_width - x)
            h = min(frame_height, sheet_height - y)

            rect = pygame.Rect(x, y, w, h)
            frame = sheet.subsurface(rect).copy()

            if scale_factor != 1:
                fw, fh = frame.get_size()
                frame = pygame.transform.scale(frame, (fw * scale_factor, fh * scale_factor))

            self.frames.append(frame)

        self.total_frames = len(self.frames)
        print(f"Successfully loaded {self.total_frames} frames into animation.")

    def get_frame(self, elapsed_time: float) -> pygame.Surface | None:
        if self.total_frames == 0:
            return None
        progress = min(1.0, max(0.0, elapsed_time / self.duration))
        frame_index = min(self.total_frames - 1, int(progress * self.total_frames))
        return self.frames[frame_index]

if __name__ == "__main__":
    print("Execution of module detected! Please run main.py for the game to work properly.")