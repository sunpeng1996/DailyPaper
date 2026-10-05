---
title: 'HelixWorld: A Real-time Interactive Audio-Visual World Model'
title_zh: HelixWorld：实时交互式音视觉世界模型
authors:
- Lei Ke
- Jiahao Pan
- Zeyue Tian
- Jiaming Wang
- Haoyuan Huang
- Kam Man Wu
- Pengjun Fang
- Hongyu Liu
- Chenyang Qi
- Lin Wang
affiliations:
- The Hong Kong University of Science and Technology
- Noiz AI
arxiv_id: '2609.38123'
url: https://arxiv.org/abs/2609.38123
pdf_url: https://arxiv.org/pdf/2609.38123
published: '2026-09-28'
collected: '2026-10-05'
category: Multimodal
direction: 多模态世界模型 · 实时音视觉交互仿真
tags:
- World-Model
- Audio-Visual-Synthesis
- Knowledge-Distillation
- Real-time-Interaction
- Multimodal-Evaluation
one_liner: 提出支持实时交互的音视觉同步世界模型，配套高保真数据集与空间声学一致性评测基准
practical_value: '- 电商虚拟逛店、3D带货直播场景可复用其音视觉同步蒸馏方案，单GPU即可实现24FPS低延迟渲染，降低算力成本

  - 具身Agent导航/交互任务可引入HelixBench的空间声学一致性评测指标，补充听觉维度的效果验证

  - 多模态虚拟场景生成任务可参考其高保真空间音视觉数据集的标注范式，优化音画对齐效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互式世界模型仅聚焦视觉渲染与控制，完全忽略声学维度，无法满足多感官沉浸式仿真需求，且实时交互延迟高、生成漂移问题突出。
### 方法关键点
1. 构建包含真实立体声学、6-DoF相机位姿的高保真空间音视觉数据集
2. 预训练基于相机轨迹与用户动作条件的双向教师模型，通过在线轨迹蒸馏loss压缩为少步流式学生模型，实现低延迟因果交互
3. 定义空间声学一致性指标，推出HelixBench评测基准，验证合成声场与动态视角运动的匹配度
### 关键结果
单GPU下可实现24FPS无漂移音视觉联合生成，视觉保真度与SOTA纯视觉世界模型持平，相机对齐的空间声学沉浸度显著超越现有基线
