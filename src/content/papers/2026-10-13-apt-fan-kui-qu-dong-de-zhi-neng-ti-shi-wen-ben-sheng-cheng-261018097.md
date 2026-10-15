---
title: 'APT: Feedback-Driven Agentic Post-Training for Text-to-Image Generation'
title_zh: APT：反馈驱动的智能体式文本生成图像模型后训练框架
authors:
- Sirui Zhang
- Fangyun Wei
- Dong Chen
- Jinjing Zhao
- Yitong Wang
- Yunuo Chen
- Baining Guo
- Zheng-Jun Zha
affiliations:
- 中国科学技术大学
- 微软亚洲研究院
- 悉尼大学
- 复旦大学
- 上海交通大学
arxiv_id: '2610.18097'
url: https://arxiv.org/abs/2610.18097
pdf_url: https://arxiv.org/pdf/2610.18097
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 智能体协作 · 生成模型后训练优化
tags:
- Agent
- Post-Training
- Text-to-Image
- Reinforcement Learning
- Self-Improvement
one_liner: 通过三个协作智能体构建自适应反馈循环，实现全自动文本生成图像模型后训练，效果优于人工构造RL训练集
practical_value: '- 电商商品图、营销海报生成的T2I模型后训练可直接复用三智能体架构：先由评估集生成智能体覆盖主图、详情页、海报等电商场景构造带rubric的评测集，诊断智能体定位模型短板（如文字错误、商品属性不符），RL数据生成智能体针对性生成训练数据，无需人工标注badcase与构造训练集

  - 生成式推荐场景的文案、图片生成模型迭代可复用自适应反馈循环逻辑：放弃固定训练集，每轮根据当前模型的能力短板动态调整训练数据分布，优先提升薄弱能力的同时保留一定比例已掌握能力样本，避免灾难性遗忘

  - 落地Agent驱动的模型优化时无需过度追求大参数LLM：实验显示从9B到122B的开源/闭源LLM均可作为RL数据生成智能体的backbone拿到相当效果，中小团队可选用低成本开源LLM降低落地门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本生成图像（T2I）模型后训练依赖人工构造训练数据，耗时费力且可扩展性差；同时固定训练集无法适配不同模型的能力分布差异，也无法随模型迭代动态调整训练优先级，导致后训练效率低、跨基准泛化性弱。
### 方法关键点
1. 三智能体协作架构：①**评估集生成智能体**：根据用户指定范围或通用评测框架，生成带专属评估rubric的prompt评测集，覆盖多场景多能力维度；②**诊断智能体**：每轮采样评测集评估当前模型，输出细粒度能力短板报告；③**RL数据生成智能体**：根据诊断报告自适应生成训练prompt，优先覆盖薄弱能力，同时保留中等、已掌握能力样本避免遗忘。
2. 迭代反馈循环：每轮RL训练后重新诊断模型，动态调整下一轮训练数据分布，实现训练任务与模型能力的耦合迭代，契合递归自我改进（RSI）思路。
3. 全框架无关设计：适配任意T2I架构（扩散、自回归）、任意评测基准，全程无需人工干预。
### 关键结果
在Lens、SD3.5、FLUX、LongCat共4个主流扩散模型，以及Janus-Pro自回归模型上验证：对比人工精心构造的RL训练集，APT在5个公开基准上平均得分高出2.65~5.49个百分点，其中FLUX模型平均得分从47.11提升至57.81；跨模型迁移APT生成的训练数据，效果比适配目标模型的原生APT低1.7~2.48个百分点。
### 核心结论
后训练的核心不仅是怎么优化模型，更是判断当前模型该学什么，自适应的动态训练数据分布效果优于精心人工构造的固定训练集
