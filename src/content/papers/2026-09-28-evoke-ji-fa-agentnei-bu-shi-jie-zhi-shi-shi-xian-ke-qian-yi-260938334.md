---
title: 'EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making'
title_zh: EVOKE：激发Agent内部世界知识实现可迁移决策
authors:
- Yuhan Guo
- Jinming Liu
- Liang Xu
- Ziqiang Li
- Jianguo Huang
- Zhicheng Wang
- Hu Zhu
- Qiuyu Chen
- Yuntao Wei
- Xin Jin
affiliations:
- Shanghai Jiaotong University
- Hong Kong Polytechnic University
- Eastern Institute of Technology, Ningbo
arxiv_id: '2609.38334'
url: https://arxiv.org/abs/2609.38334
pdf_url: https://arxiv.org/pdf/2609.38334
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: LLM Agent 可迁移决策训练优化
tags:
- LLM Agent
- World Knowledge
- Preference Learning
- Transfer Learning
- LoRA
one_liner: 通过固定状态下多目标动作偏好排序，激发LLM预训练内置世界知识，显著提升Agent跨环境迁移能力
practical_value: '- 电商导购Agent、搜索推荐Agent训练可直接复用「固定状态+多目标偏好标注」范式，无需额外训练世界模型预测模块，大幅降低训练成本的同时提升跨场景迁移能力

  - 做对比学习/偏好训练时，优先选取当前模型自身倾向输出的错误结果作为hard negative，训练效率比随机负样提升40%以上，可直接复用在推荐排序、Query改写等场景

  - 小参数LLM（如1.7B/3B）用该范式训练的增益远高于大模型，业务预算有限时可优先尝试小模型+EVOKE训练，无需盲目堆大参数模型

  - 配合多轮DAgger式数据聚合，仅需原SFT 10%左右的标注数据就能实现更好的泛化效果，适合Agent冷启动、标注资源不足的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent在未知环境下迁移性能骤降，传统世界模型方法需要新增动作后果预测目标，训练成本高且预测误差会沿决策链累计；而LLM预训练阶段已经内化了数字场景下绝大多数动作规则知识，常规单目标SFT/RL训练仅会让Agent拟合上下文惯性动作，不会触发内置世界知识的调用，导致泛化能力差。
### 方法关键点
- 固定环境状态、交互历史、候选动作集，替换不同目标迫使相同动作的偏好排序反转，彻底切断Agent依赖上下文习惯做决策的路径，必须调用内置的动作后果知识才能正确排序
- 标注阶段优先选取当前策略输出的高概率错误动作作为hard negative，大幅提升训练效率
- 采用列表式+配对式组合的对比排序损失训练LoRA权重，无需修改LLM主干，部署阶段无额外推理开销
- 多轮迭代聚合数据，每轮用更新后的策略采集新状态，持续对齐当前策略的错误点
### 关键实验
在ALFWorld、WebShop、搜索QA三类任务，Qwen3-1.7B、Qwen2.5-3B/7B三个骨干上测试，对比GRPO、世界模型类等20+基线：ALFWorld unseen场景3B模型成功率达91.1%，超出最强基线5.2个点；WebShop成功率达82.8%，超出基线14.8个点；仅用9%的原SFT标注数据量，效果就超过全量SFT的泛化性能。
### 核心结论
LLM作为Agent的大部分世界知识已经内置在预训练权重中，核心问题不是如何给模型注入新知识，而是如何设计训练信号让模型把已有的知识真正用到决策里
