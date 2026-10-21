---
title: Focused Omni-Modal GUI Agents
title_zh: FocusGUI：适配多步交互的全模态GUI智能体感知优化方法
authors:
- Fuyao Zhang
- Wenwen He
- Jiaming Zhang
- Yurong Hao
- Xuan Wang
- Guowei Guan
- Che Wang
- Longtao Huang
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
- Alibaba Group
arxiv_id: '2610.26203'
url: https://arxiv.org/abs/2610.26203
pdf_url: https://arxiv.org/pdf/2610.26203
published: '2026-10-18'
collected: '2026-10-21'
category: Agent
direction: GUI Agent · 全模态多步交互优化
tags:
- GUI Agent
- Multimodal
- Adapter
- Sequential Interaction
- Frozen Backbone
one_liner: 轻量零初始化残差适配器，无需微调主干即可大幅提升全模态GUI Agent多步交互准确率
practical_value: '- 电商导购Agent、运营自动化Agent落地时，无需微调大参数量全模态主干，仅新增1M左右可训练参数的FocusGUI适配器即可大幅提升多步操作准确率，显著降低训练成本和上线风险

  - 语音+视觉的短视频/直播互动Agent场景可复用动态通道加权机制，避免硬裁剪多模态输入丢失坐标、上下文等关键信息，同时解决长序列交互的注意力漂移问题

  - 零初始化残差注入技巧可迁移到各类生成式推荐、业务Agent场景，在不破坏主干原有能力的前提下注入业务定制信号，无需重新对齐输出空间'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态GUI Agent在多步交互中，每步决策依赖的模态信息是动态变化的：相邻步骤间主导模态切换比例达45.3%，90%的步骤存在干扰模态，统一输入全量上下文会导致**Sequential Distraction**，错误逐步累积造成轨迹不可逆偏离；现有裁剪/局部放大视觉输入的方法会丢失坐标、文本等必要上下文，也覆盖不到音频、视频时序等非视觉信号，Exact Match反而下降28%。

### 方法关键点
- 主干模型全冻结，仅新增1.15M-1.45M可训练参数的轻量适配器，仅靠动作标注监督训练，无需模态相关性标注
- 将输入拆分为屏幕、音频、视频、交互历史等独立感知通道，基于当前步全量观测生成决策参考，动态计算各通道优先级，加权后压缩为64维低维聚焦表征
- 零初始化残差注入到动作生成前的4个prompt嵌入位置，不修改原有输入和主干结构，完整保留全量上下文信息

### 关键实验
在OmniGUI基准（覆盖29个手机应用，708个交互序列共2572个动作步骤）上测试4个主流全模态主干：平均相比原生冻结主干提升Type Match 33.2个百分点，Exact Match提升3倍；比最强现有增强方法提升Type Match 30.1个百分点；多步交互到第4步时原生主干Type Match下降50%，FocusGUI仅下降13.2%。

### 核心结论
多步交互场景下，优化模型对输入的读取优先级，远好于直接裁剪输入，且可以完全保留主干模型的原有能力。
