"""骨骼姿态预设 — 常用动作的骨骼旋转数据（弧度）

支持两种骨骼系统:
  - MPFB2 标准骨骼（rig.default.json, 163 bones）
  - Mixamo 骨骼（rig.mixamo.json, 52 bones）

旋转顺序为 (X, Y, Z)，符合 Blender 默认 XYZ Euler。
"""

# ── Mixamo 骨骼映射 ──────────────────────────────────────
# Mixamo 用 mixamorig: 前缀，命名与 MPFB2 不同
MIXAMO_BONES = {
    "Hips": "mixamorig:Hips",
    "Spine": "mixamorig:Spine",
    "Spine1": "mixamorig:Spine1",
    "Spine2": "mixamorig:Spine2",
    "Neck": "mixamorig:Neck",
    "Head": "mixamorig:Head",
    "LeftShoulder": "mixamorig:LeftShoulder",
    "LeftArm": "mixamorig:LeftArm",
    "LeftForeArm": "mixamorig:LeftForeArm",
    "LeftHand": "mixamorig:LeftHand",
    "RightShoulder": "mixamorig:RightShoulder",
    "RightArm": "mixamorig:RightArm",
    "RightForeArm": "mixamorig:RightForeArm",
    "RightHand": "mixamorig:RightHand",
    "LeftUpLeg": "mixamorig:LeftUpLeg",
    "LeftLeg": "mixamorig:LeftLeg",
    "LeftFoot": "mixamorig:LeftFoot",
    "LeftToeBase": "mixamorig:LeftToeBase",
    "RightUpLeg": "mixamorig:RightUpLeg",
    "RightLeg": "mixamorig:RightLeg",
    "RightFoot": "mixamorig:RightFoot",
    "RightToeBase": "mixamorig:RightToeBase",
}


def _mpfb2_pose(bone_rotations: dict) -> dict:
    """MPFB2 标准骨骼预设（不变）"""
    return bone_rotations


def _mixamo_pose(bone_rotations: dict) -> dict:
    """将通用骨骼名转换为 Mixamo 骨骼名"""
    return {MIXAMO_BONES.get(k, k): v for k, v in bone_rotations.items()}


# ── 通用骨骼预设（内部用 MPFB2 风格定义）──────────────────
_GENERIC_PRESETS = {
    "t-pose": {},
    "standing": {
        "upperarm01.L": (0, 0, 0.3),
        "upperarm01.R": (0, 0, -0.3),
        "lowerarm01.L": (0, 0, -0.1),
        "lowerarm01.R": (0, 0, 0.1),
    },
    "arms_up": {
        "upperarm01.L": (1.5, 0, 0),
        "upperarm01.R": (1.5, 0, 0),
        "lowerarm01.L": (0, 0, 0),
        "lowerarm01.R": (0, 0, 0),
    },
    "walk_left": {
        "upperleg01.L": (0.5, 0, 0),
        "lowerleg01.L": (-0.8, 0, 0),
        "upperarm01.L": (-0.3, 0, 0),
        "lowerarm01.L": (-0.4, 0, 0),
    },
    "walk_right": {
        "upperleg01.R": (-0.5, 0, 0),
        "lowerleg01.R": (0.8, 0, 0),
        "upperarm01.R": (0.3, 0, 0),
        "lowerarm01.R": (0.4, 0, 0),
    },
    "wave": {
        "upperarm01.L": (1.5, 0, 0.2),
        "lowerarm01.L": (2.0, 0, 0),
        "lowerarm02.L": (0, 0, -0.3),
    },
    "sit": {
        "upperleg01.L": (1.5, 0, 0),
        "upperleg01.R": (1.5, 0, 0),
        "lowerleg01.L": (-1.5, 0, 0),
        "lowerleg01.R": (-1.5, 0, 0),
    },
    "run": {
        "upperleg01.L": (0.9, 0, 0),
        "lowerleg01.L": (-1.2, 0, 0),
        "upperleg01.R": (-0.6, 0, 0),
        "lowerleg01.R": (0.3, 0, 0),
        "upperarm01.L": (-0.5, 0, 0),
        "lowerarm01.L": (-0.6, 0, 0),
        "upperarm01.R": (0.5, 0, 0),
        "lowerarm01.R": (0.6, 0, 0),
        "spine01": (-0.1, 0, 0),
        "spine02": (-0.1, 0, 0),
    },
    "fighting_stance": {
        "upperleg01.L": (0.3, 0.1, 0),
        "lowerleg01.L": (-0.6, 0, 0),
        "upperleg01.R": (-0.2, -0.1, 0),
        "lowerleg01.R": (-0.3, 0, 0),
        "upperarm01.L": (0.8, 0.5, 0.3),
        "lowerarm01.L": (-1.5, 0, 0),
        "upperarm01.R": (0.6, -0.3, -0.2),
        "lowerarm01.R": (-1.2, 0, 0),
        "spine02": (0, 0, 0.1),
    },
    "hands_on_hips": {
        "upperarm01.L": (0, 0, 0.8),
        "lowerarm01.L": (1.5, 0, 0),
        "upperarm01.R": (0, 0, -0.8),
        "lowerarm01.R": (1.5, 0, 0),
    },
    "crossed_arms": {
        "upperarm01.L": (0, 0, 0.8),
        "lowerarm01.L": (1.8, 0, 0),
        "upperarm01.R": (0, 0, -0.8),
        "lowerarm01.R": (1.8, 0, 0),
    },
    "sitting_relaxed": {
        "upperleg01.L": (1.5, 0, 0),
        "upperleg01.R": (1.5, 0, 0),
        "lowerleg01.L": (-1.5, 0, 0),
        "lowerleg01.R": (-1.5, 0, 0),
        "upperarm01.L": (0, 0, 0.5),
        "lowerarm01.L": (1.2, 0, 0),
        "upperarm01.R": (0, 0, -0.5),
        "lowerarm01.R": (1.2, 0, 0),
        "spine02": (-0.1, 0, 0),
    },
}

# ── Mixamo 专用预设 ─────────────────────────────────────
# Mixamo 骨骼名与 MPFB2 完全不同，直接用 mixamorig: 命名
MIXAMO_POSE_PRESETS = {
    "t-pose": {},
    "standing": {
        "mixamorig:LeftArm": (0, 0, 0.3),
        "mixamorig:RightArm": (0, 0, -0.3),
        "mixamorig:LeftForeArm": (0, 0, -0.1),
        "mixamorig:RightForeArm": (0, 0, 0.1),
    },
    "arms_up": {
        "mixamorig:LeftArm": (1.5, 0, 0),
        "mixamorig:RightArm": (1.5, 0, 0),
    },
    "walk_left": {
        "mixamorig:LeftUpLeg": (0.5, 0, 0),
        "mixamorig:LeftLeg": (-0.8, 0, 0),
        "mixamorig:LeftArm": (-0.3, 0, 0),
        "mixamorig:LeftForeArm": (-0.4, 0, 0),
    },
    "walk_right": {
        "mixamorig:RightUpLeg": (-0.5, 0, 0),
        "mixamorig:RightLeg": (0.8, 0, 0),
        "mixamorig:RightArm": (0.3, 0, 0),
        "mixamorig:RightForeArm": (0.4, 0, 0),
    },
    "wave": {
        "mixamorig:LeftArm": (1.5, 0, 0.2),
        "mixamorig:LeftForeArm": (2.0, 0, 0),
    },
    "sit": {
        "mixamorig:LeftUpLeg": (1.5, 0, 0),
        "mixamorig:RightUpLeg": (1.5, 0, 0),
        "mixamorig:LeftLeg": (-1.5, 0, 0),
        "mixamorig:RightLeg": (-1.5, 0, 0),
    },
    "run": {
        "mixamorig:LeftUpLeg": (0.9, 0, 0),
        "mixamorig:LeftLeg": (-1.2, 0, 0),
        "mixamorig:RightUpLeg": (-0.6, 0, 0),
        "mixamorig:RightLeg": (0.3, 0, 0),
        "mixamorig:LeftArm": (-0.5, 0, 0),
        "mixamorig:LeftForeArm": (-0.6, 0, 0),
        "mixamorig:RightArm": (0.5, 0, 0),
        "mixamorig:RightForeArm": (0.6, 0, 0),
        "mixamorig:Spine": (-0.1, 0, 0),
        "mixamorig:Spine1": (-0.1, 0, 0),
    },
    "fighting_stance": {
        "mixamorig:LeftUpLeg": (0.3, 0.1, 0),
        "mixamorig:LeftLeg": (-0.6, 0, 0),
        "mixamorig:RightUpLeg": (-0.2, -0.1, 0),
        "mixamorig:RightLeg": (-0.3, 0, 0),
        "mixamorig:LeftArm": (0.8, 0.5, 0.3),
        "mixamorig:LeftForeArm": (-1.5, 0, 0),
        "mixamorig:RightArm": (0.6, -0.3, -0.2),
        "mixamorig:RightForeArm": (-1.2, 0, 0),
        "mixamorig:Spine1": (0, 0, 0.1),
    },
    "hands_on_hips": {
        "mixamorig:LeftArm": (0, 0, 0.8),
        "mixamorig:LeftForeArm": (1.5, 0, 0),
        "mixamorig:RightArm": (0, 0, -0.8),
        "mixamorig:RightForeArm": (1.5, 0, 0),
    },
    "crossed_arms": {
        "mixamorig:LeftArm": (0, 0, 0.8),
        "mixamorig:LeftForeArm": (1.8, 0, 0),
        "mixamorig:RightArm": (0, 0, -0.8),
        "mixamorig:RightForeArm": (1.8, 0, 0),
    },
    "sitting_relaxed": {
        "mixamorig:LeftUpLeg": (1.5, 0, 0),
        "mixamorig:RightUpLeg": (1.5, 0, 0),
        "mixamorig:LeftLeg": (-1.5, 0, 0),
        "mixamorig:RightLeg": (-1.5, 0, 0),
        "mixamorig:LeftArm": (0, 0, 0.5),
        "mixamorig:LeftForeArm": (1.2, 0, 0),
        "mixamorig:RightArm": (0, 0, -0.5),
        "mixamorig:RightForeArm": (1.2, 0, 0),
        "mixamorig:Spine1": (-0.1, 0, 0),
    },
}


def get_pose_preset(name: str, rig_type: str = "mpfb2") -> dict:
    """获取骨骼姿态预设

    Args:
        name: 预设名（t-pose, standing, walk_left 等）
        rig_type: 骨骼类型 "mpfb2" 或 "mixamo"

    Returns:
        骨骼旋转字典 {bone_name: (rx, ry, rz)}
    """
    if rig_type == "mixamo":
        return dict(MIXAMO_POSE_PRESETS.get(name, {}))
    return dict(_GENERIC_PRESETS.get(name, {}))


# ── 向后兼容 ─────────────────────────────────────────────
# 原代码直接引用 POSE_PRESETS，保持不变
POSE_PRESETS = _GENERIC_PRESETS
