---
title: 'AdaGuard: An Adaptive Guard Model with User-defined Policies'
title_zh: AdaGuard：支持用户自定义策略的自适应Agent安全防护模型
authors:
- Yunhao Feng
- Yifan Ding
- Yuxiang Xie
- Zheng Li
- Mingrui Lao
- Zeyuan Wang
- Yanming Guo
affiliations:
- National University of Defense Technology
- Fudan University
arxiv_id: '2609.34241'
url: https://arxiv.org/abs/2609.34241
pdf_url: https://arxiv.org/pdf/2609.34241
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: Agent安全防护 · 自定义策略合规校验
tags:
- Agent Safety
- Guardrail Model
- Reinforcement Learning
- Custom Policy
- Dataset Augmentation
one_liner: 构建反事实增强的自适应安全数据集+SafePO强化学习算法，实现可自定义策略的Agent行为安全校验
practical_value: '- 电商/广告业务侧的Agent（客服、智能运营、权益发放等）合规校验可直接复用该框架，无需为每个场景单独训练Guard模型，仅需传入对应业务自定义规则即可实现全轨迹合规判定

  - 训练同时需要输出自然语言解释和结构化结果的任务时，可复用SafePO的权重分配机制：固定解释区和核心输出区的权重比例，避免长解释稀释核心输出的学习信号，同时用结构化奖励区分不同错误类型的输出，提升核心指标

  - 规则匹配类任务标注成本高时，可借鉴三类数据增强方法：结构增强（调整规则顺序/ID）、策略反事实（固定输入改规则）、行为反事实（固定规则改输入），快速生成配对训练样本，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Guard模型依赖固定风险分类体系，无法适配不同业务场景的差异化安全要求：例如电商场景下发送文件在客诉场景被允许、在商家敏感数据导出场景被禁止，相同Agent行为在不同规则下判定结果完全不同；同时现有自适应Guard大多仅覆盖对话内容安全，未支持Agent工具调用、环境交互的全轨迹校验。

### 方法关键点
- 构建AdaptiveSafety数据集：包含10939条训练样本、1000条测试样本，覆盖含1-100条规则的自定义策略，通过三类增强生成样本：结构增强（调整规则顺序、ID、新增无关规则）、策略反事实（固定Agent轨迹修改规则）、行为反事实（固定规则修改Agent行为/工具返回结果），每条样本配套解释和违规规则ID标注
- 提出SafePO强化学习算法：设计结构化奖励区分完全匹配、规则正确但顺序错误、部分匹配、格式错误的输出，SFT阶段给标签区域分配4倍权重；组内归一化奖励获得响应级优势，消除不同任务难度的干扰；独立价值模型调整解释区和判决区的token权重，固定两区权重比例1:2，保证短判决区域获得足够学习信号
- 训练得到0.6B/4B/8B三个规格的AdaGuard模型，推理时直接传入自定义策略即可完成Agent轨迹合规校验

### 关键实验
在AdaptiveSafety测试集上，AdaGuard-4B二进制准确率达89.30%，较最强非AdaGuard基线高22.2个百分点；在DynaBench公开数据集上准确率达71.82%，同时支持输出具体违规的规则ID，AdaGuard-8B的规则集完全匹配率达70.72%。

**最值得记住的一句话**：面向多场景的规则类校验任务，与其为每个场景训练专用模型，不如用支持动态策略输入的通用模型，配合结构化奖励强化核心输出的准确性，落地性价比更高
