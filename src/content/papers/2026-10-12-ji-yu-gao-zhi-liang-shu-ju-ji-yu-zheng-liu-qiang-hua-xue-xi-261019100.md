---
title: 'GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement
  Learning'
title_zh: 基于高质量数据集与蒸馏强化学习的GUI定位框架GroundGUI
authors:
- Qingsong Xie
- Jiahao Tian
- Jiacheng Tang
- Zhifeng Li
- Madalina Ciobanu
- Navan Preet Singh
- Qingqing Mao
- Ritankar Das
affiliations:
- Prentis AI
- Westlake University
- Titan Holdings
arxiv_id: '2610.19100'
url: https://arxiv.org/abs/2610.19100
pdf_url: https://arxiv.org/pdf/2610.19100
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: GUI Agent · 多模态界面定位
tags:
- GUI Grounding
- Multi-modal Agent
- Reinforcement Learning
- Self-distillation
- Open Dataset
one_liner: 开源跨端GUI定位数据集与蒸馏强化训练框架，8B模型实现同规模SOTA性能
practical_value: '- 做电商界面自动化Agent（自动投放、竞品爬取、客服操作机器人等）时，可直接复用开源GroundGUI-8B作为界面元素定位基座，降低多端界面适配成本

  - 小参数模型强化训练可借鉴D2RL框架：先做带特权信息的On-Policy Self-Distillation生成高质量初始策略，再做RLOO强化，解决稀疏奖励问题，该思路可迁移到广告动态出价、长序列推荐路径优化等序列决策任务

  - 构建多模态训练数据集时可复用ScreenRef的双路数据构建+多级校验pipeline：静态截图爬取+操作视频关键帧提取搭配大模型自动校验，大幅降低标注成本，可用于电商商品图文对标注、短视频操作类指令数据集构建

  - 坐标生成类任务训练时可加入位置感知加权：对高位坐标digit赋予更高loss权重，提升定位精度，该trick可迁移到图像商品定位、热点区域点击预测等任务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GUI定位（将自然语言指令映射到界面可交互元素坐标）是跨端GUI Agent的核心基础能力，现有开源数据集存在覆盖场景少、标注精度低、缺少不可行请求拒绝样本等问题；纯SFT训练泛化性差易过拟合，纯RL训练存在稀疏奖励瓶颈，小参数模型难以在跨端GUI定位任务上达到商用精度。

### 方法关键点
- **数据集**：开源ScreenRef数据集，包含586K跨端（桌面/网页/移动端）截图、633K指代表达，覆盖文本识别、视觉匹配、空间理解、不可行请求拒绝4类任务，通过静态截图爬取+教程视频关键帧提取双路pipeline + 多级大模型校验保证标注质量
- **训练框架**：提出D2RL两阶段训练范式，第一阶段OPSD：用带目标框高亮特权信息的冻结教师模型，对学生模型的生成轨迹做带位置感知加权的自蒸馏，生成高质量初始策略；第二阶段RLOO：用点在框内二值奖励做强化学习优化，无需单独critic，解决稀疏奖励问题
- **模型**：基于Qwen3-VL-8B-Instruct做SFT+D2RL训练，得到GroundGUI-8B模型

### 关键结果
在5个主流GUI定位基准上达到同规模SOTA：ScreenSpot-V2 95.2%、ScreenSpot-Pro 63.9%、OSWorld-G 65.4%、MMBench-GUI L2 86.8%、UI-Vision 38.3%，性能超过多个闭源8B模型和32B开源模型；相比纯SFT baseline平均提升1.9个百分点，相比纯RL训练平均提升1个百分点。

### 核心结论
带特权信息的自蒸馏预处理是解决强化学习稀疏奖励问题的低成本有效路径，高质量场景覆盖的数据集比大参数量对垂直领域任务的提升更显著
