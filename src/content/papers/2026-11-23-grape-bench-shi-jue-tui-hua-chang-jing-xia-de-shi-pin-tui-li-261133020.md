---
title: 'GRAPE-Bench: When Vision Degrades, Does Video Reasoning Hold?'
title_zh: GRAPE-Bench：视觉退化场景下的视频推理能力评测基准
authors:
- Ce Zhang
- Junyi He
- Tianshi Ming
- Jinxi He
- Jianshu Zhang
- Xiyuan Yang
- Jianuo Zhu
- Yicheng Tao
- Xiyu Luo
- Minghao Fu
affiliations:
- CMU
- Northwestern
- UIUC
- UCSD
- NUS
arxiv_id: '2611.33020'
url: https://arxiv.org/abs/2611.33020
pdf_url: https://arxiv.org/pdf/2611.33020
published: '2026-11-23'
collected: '2026-11-25'
category: Eval
direction: 多模态大模型 · 视频推理鲁棒性评测
tags:
- MLLM
- Video Reasoning
- Robustness
- Benchmark
- Degraded Vision
one_liner: 推出覆盖合成/真实退化场景、分难度的视频推理鲁棒性评测基准GRAPE-Bench
practical_value: '- 短视频/直播推荐的多模态理解模块，可参考该基准的退化场景构造方法，测试低清晰度、极端光线等劣化内容下的标签识别、内容理解准确率，减少badcase。

  - 多模态Agent（如直播场控Agent、户外商品巡检Agent）可借鉴分难度评测思路，优先保障高优先级基础判断准确率，再优化高阶推理能力。

  - 劣化输入下的模型性能优化，可复用合成退化数据微调+偏好steering方案，在整体精度几乎不变的前提下倾斜核心任务优先级。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频推理基准多基于高质量输入，仅模拟视觉退化或仅做高难度推理测试，无法覆盖真实恶劣场景的鲁棒性需求，也无法区分不同难度任务的表现差异，难以支撑自动驾驶等安全敏感场景的模型验证。

### 方法关键点
1. 构建合成+真实双赛道退化视频集，覆盖12类合成退化类型、以及雨天/雪天/雾天/夜间等真实驾驶场景；
2. 每个视频匹配3级难度问题，从安全相关基础判断到高阶推理压力测试，可分层评估模型能力；
3. 提出合成数据微调、洁净数据蒸馏、偏好steering三类优化方案。

### 关键结果
- 合成数据微调将Qwen3.5-9B真实场景准确率从76.7%提升至81.1%；
- 洁净数据蒸馏在推理使能设置下达到80.4%准确率；
- 偏好steering可在整体精度几乎不变的前提下，连续调节模型在安全判断和高阶推理间的trade-off。
