---
title: 'Latent-IM: Latent Interaction Management for Speech LLMs'
title_zh: Latent-IM：面向语音大模型的潜在交互管理框架
authors:
- Adar Avsian
- Atahan Dokme
- Tony Woo
- Larry Heck
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.26928'
url: https://arxiv.org/abs/2607.26928
pdf_url: https://arxiv.org/pdf/2607.26928
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM激活转向 · 对话行为控制
tags:
- Activation Steering
- Dialogue Management
- Speech LLM
- Controllable Generation
- Frozen LLM
one_liner: 在冻结语音LLM内还原对话管理流程，通过激活转向实现可控对话动作生成，效果媲美微调
practical_value: '- 可复用激活转向框架，无需微调大模型即可控制Agent生成的话术动作（比如电商客服的确认、询问、解释动作），降低LoRA微调的成本和数据依赖

  - 可迁移「选择-实现」解耦设计：先从LLM残差流读取当前最优动作，再用预训练动作方向向量控制生成，比直接Prompt控制准确率高10+个百分点

  - 对话长度控制trick可直接落地：通过预计算的turn-boundary方向向量，生成时注入即可单调控制回复长度，适配不同场景的回复长度需求

  - 自动评估方法可复用：用大模型少样本分类器做生成动作的自动校验，和人工标注一致性达73.9%，大幅降低对话类系统的评测成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端到端LLM对话系统将传统对话管理的状态跟踪、动作选择逻辑隐式封装在模型内部，无法可控引导对话动作（如何时确认需求、何时询问信息、何时直接回复），微调成本高，Prompt控制效果不稳定，亟需无需修改模型权重的LLM对话行为控制方案。

### 方法关键点
- 框架解耦为选择、实现两个模块：选择模块是轻量流式SSM控制器，读取冻结语音LLM的残差流激活，预测下一个对话动作（共5类：acknowledge、check、explain、query、reply）和回复长度
- 实现模块通过预计算的动作专属激活方向向量，生成时注入指定Transformer层，引导模型输出对应动作的回复，无需修改模型权重
- 加入实现感知门控：仅对转向效果好的动作（check、query、explain）注入激活向量，对转向效果差的reply动作使用原生生成，仅对短动作注入长度控制向量，避免效果损失
- 预计算turn-boundary方向向量，可单调控制回复长度，无需额外逻辑

### 关键实验
在3个任务型对话数据集MapTask、FindTask、CReST上验证，对比基线包括Prompt控制、FUDGE、DeAL、LoRA SFT等：
- 动作选择平均准确率达0.60，超过所有基于文本的选择器
- Oracle实现平均准确率60%，比最优基线高10.4个百分点
- 端到端动作准确率46.9%，比原生LLM高12.5个百分点，和LoRA微调效果（46.6%）相当
- 长度控制可将平均回复长度在10.4~71.3词之间单调调节

### 最值得记住的一句话
冻结LLM的残差流已经包含足够的对话状态信息，只需轻量侧车模块读取+激活转向就能媲美微调的可控生成效果，无需修改模型权重
