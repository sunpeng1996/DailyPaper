---
title: 'SceneActBench: Can Agents Act on the 3D Scenes They See?'
title_zh: SceneActBench：3D场景下视觉驱动智能体行动能力评测基准
authors:
- Yifei Zhao
- Xiangxin Zhou
- Wenhao Yang
- Jiaqi Tang
- Pu Jian
- Huanjin Yao
- Jiarui Yao
- Haowei Lin
- Chunchao Guo
- Zhuo Chen
affiliations:
- Tencent Hunyuan
- Tsinghua University
- Nanjing University
- Hong Kong University of Science and Technology
- Peking University
arxiv_id: '2607.22393'
url: https://arxiv.org/abs/2607.22393
pdf_url: https://arxiv.org/pdf/2607.22393
published: '2026-07-23'
collected: '2026-07-27'
category: Eval
direction: 智能体评测 · 3D场景视觉行动
tags:
- VLM Agent
- 3D Scene Understanding
- Benchmark
- Embodied AI
- Vision-Language Model
one_liner: 提出统一Agent-环境交互范式的3D场景智能体行动评测基准，覆盖5类任务共520个测试用例
practical_value: '- 家居/家装电商3D导购Agent落地时，可复用该基准的任务设计逻辑，验证Agent空间操作（如家具摆放、场景适配）的准确性

  - 多任务Agent评测体系建设可参考其统一Agent-环境交互环的设计，消除不同任务评测逻辑差异带来的结果偏差

  - 多模态VLM Agent效果评估可引入其几何匹配指标，补充纯文本语义匹配之外的落地效果评估维度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM Agent已可通过工具实现3D场景操作而非仅做场景描述，但现有3D相关基准仅评测文本输出或单物体操作，多物体完整3D场景下的Agent行动能力缺乏系统性评估。
### 方法关键点
1. 构建统一Agent-环境交互环路的SceneActBench基准，覆盖布局规划、相机操控、关节物体操作、3D重建、动态场景交互5类核心3D任务
2. 基于210个源实例生成520个带配对输入条件的测试用例，所有任务采用固定交互环保证评测公平性
3. 针对每个任务设计专属几何评估指标，对比Agent最终输出与隐藏真值的匹配度，而非仅评估文本回复
### 关键结果
测试11款商用VLM配置，整体得分区间为38.6~50.2，无模型在所有任务上均表现稳定优异，同时明确了VLM Agent在3D场景操作中的典型失效模式
