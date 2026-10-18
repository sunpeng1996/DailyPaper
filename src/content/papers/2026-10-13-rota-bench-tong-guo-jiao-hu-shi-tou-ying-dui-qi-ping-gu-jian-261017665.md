---
title: 'RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection
  Alignment'
title_zh: RoTA-Bench：通过交互式投影对齐评估3D空间推理能力
authors:
- Qingchuan Ma
- Yuexiao Ma
- Xiang Meng
- Yixuan Zou
- Tianyu Xie
- Wang Chen
- Yuhui Zeng
- Yuhang Wu
- Xiawu Zheng
- Rongrong Ji
affiliations:
- 厦门大学教育部多媒体可信感知与高效计算重点实验室
- 南洋理工大学CCDS
- 厦门大学人工智能研究院
arxiv_id: '2610.17665'
url: https://arxiv.org/abs/2610.17665
pdf_url: https://arxiv.org/pdf/2610.17665
published: '2026-10-13'
collected: '2026-10-18'
category: Eval
direction: 多模态模型 · 3D空间推理能力评测
tags:
- Spatial Reasoning
- Evaluation Benchmark
- Vision-Language Model
- 3D Understanding
- Embodied Agent
one_liner: 构建交互式3D-2D投影对齐基准RoTA-Bench，评测多模态模型3D空间推理与交互控制能力
practical_value: '- 优化3D商品展示、AR试穿类Agent交互逻辑时，可参考RoTA-Bench的交互反馈机制，调整视角操作粒度，提升用户操作精准度

  - 构建AR导购、3D内容生成类多模态模型评测集时，可复用可逆初始化构造可解任务的方法，降低数据集构建成本

  - 开发交互类Agent动作规划模块时，需保留完整交互历史上下文，避免粗粒度操作导致任务成功率大幅下降'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型的3D空间推理、基于视觉反馈的精细化控制能力缺乏统一交互式评测基准，无法验证其将2D观测转化为3D理解并指导精准动作的能力。
### 方法关键点
构建RoTA-Bench评测框架，核心任务为给定目标轮廓，控制3D物体旋转，在有限步数内将投影对齐到目标轮廓；通过自动流水线从2D图标生成保留轮廓的3D物体，引入可逆初始化保证任务可解，共构造674个任务、100个分层测试集。
### 关键结果
1. 人模差距显著，GPT-5.6-Sol任务成功率仅17%，人类测试者成功率达100%
2. 模型更易出现轮廓重叠提升但姿态对齐恶化的情况，占比19.4%，远高于人类的10.9%
3. 移除交互历史后，96.8%的模型操作退化为30度粗粒度步长，任务成功率骤降
