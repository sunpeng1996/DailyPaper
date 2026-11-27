---
title: Audio-Visual Rearrangement
title_zh: 视听模态具身重排（AVR）：语音指令驱动的物品递送任务与方法
authors:
- Ruohao Guo
- Jiatong Ye
- Chenwei Dong
- Jinxing Zhou
- Dantong Niu
- Guangyao Li
- Zhenbo Li
affiliations:
- China Agricultural University
- Mohamed bin Zayed University of Artificial Intelligence
- University of California, Berkeley
arxiv_id: '2611.30171'
url: https://arxiv.org/abs/2611.30171
pdf_url: https://arxiv.org/pdf/2611.30171
published: '2026-11-23'
collected: '2026-11-27'
category: Agent
direction: 具身Agent · 多模态指令理解与执行
tags:
- Embodied-Agent
- Multimodal-LLM
- Instruction-Tuning
- Audio-Visual-Perception
- Human-Robot-Interaction
one_liner: 提出语音驱动的视听具身物品重排任务，构建数据集及融合空间音频的多模态大模型基线
practical_value: '- 语音交互类导购Agent、服务机器人场景可复用「运动感知空间音频模块+多模态LLM」的架构，提升多模态指令理解与执行准确率

  - 多任务instruction tuning引入语音理解、空间感知、视觉grounding三类辅助监督的trick，可迁移至多模态推荐系统的用户意图理解模块优化

  - 显式目标、相对空间参考、隐含用户意图三类query分类体系，可直接用于语音交互类搜索推荐的query类型打标与逻辑路由'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有具身多模态研究未统一覆盖隐含意图理解、说话人定位、物品操作全链路能力，无法支撑服务机器人基于自然语音指令完成物品递送的真实场景需求。
### 方法关键点
1. 提出AVR新任务，要求Agent听懂语音请求、声学定位说话人、检索匹配物品并递送至指定位置；
2. 构建覆盖显式目标指定、说话人相对空间参考、隐含用户意图3类共8种子类型的数据集，适配多样物品选择与递送要求；
3. 向视听大模型中集成运动感知空间音频模块，编码语音请求的空间线索并随Agent移动动态更新，引入三类辅助监督做多任务instruction tuning优化动作预测。
### 关键结果
完成已见/未见环境下的基线性能测试，为后续具身智能与人机交互研究提供基准支撑。
