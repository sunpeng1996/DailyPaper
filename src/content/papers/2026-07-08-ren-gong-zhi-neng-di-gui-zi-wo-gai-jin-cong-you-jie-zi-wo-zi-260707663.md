---
title: 'Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous
  Research Loops'
title_zh: 人工智能递归自我改进：从有界自我优化到自主研究闭环
authors:
- Mingguang Chen
- Licheng Wang
- Bo Qu
affiliations:
- University of California, Riverside
- AlphaAvatar
- Illinois Institute of Technology
arxiv_id: '2607.07663'
url: https://arxiv.org/abs/2607.07663
pdf_url: https://arxiv.org/pdf/2607.07663
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 递归自我改进框架与分类
tags:
- Recursive Self-Improvement
- Self-Evaluation
- Agent
- Self-Refine
- Taxonomy
one_liner: 梳理2024-2026年1250篇递归自我改进论文，提出两轴分类框架并明确自评估是核心瓶颈
practical_value: '- 落地LLM Agent迭代时，优先将自评估信号向验证层级上层迁移：可执行规则（如订单校验、SQL跑测）> 结构化PRM >
  自由格式LLM Judge > 模型内在自评估，规避自证循环与效果退化

  - 用自生成数据做训练（如推荐文案生成模型SFT、Agent执行策略优化）时，必须混入至少10%的外部ground truth数据做锚定，避免多轮迭代后出现效果或多样性崩溃

  - 初期优先落地低风险自改进场景：推理阶段输出自我修正、prompt/skill库自动迭代优化，暂不碰权重级完全闭环自训练，降低回滚成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前递归自我改进（RSI）领域术语体系混乱，self-refine、self-reward、self-play等概念定义交叉，技术迭代极快但缺乏统一分类框架，工业界落地、安全治理均无清晰的技术边界和瓶颈识别依据。
### 方法关键点
- 构建覆盖2024-2026年arXiv的1250篇RSI相关论文语料，涵盖自我修正、自奖励训练、自动化AI研究等7个核心方向
- 提出两轴分类框架：横轴为改进对象（部署阶段行为/训练阶段策略/自评估器/研究流程本身），纵轴为闭环程度（人在环内/人在环上/完全闭环），清晰区分有界自我优化与开放RSI边界
- 搭建自评估信号验证层级：按可靠性从高到低排序为形式化验证器>执行反馈>学习型Judge>模型内在自评估信号，明确不同信号对应的改进效果天花板
### 关键结果
- 语料中74%的论文发表于2026年，2026年Q2单季度发文量达500篇，领域增速远超现有综述覆盖节奏
- 部署阶段自我优化、训练阶段自迭代、自评估、自动研究四类核心方向的论文占比分别为31.4%、27.2%、25.4%、11.1%，自评估相关论文2026年占比达82%，是当前最热方向
- 无外部grounding的纯自评估闭环迭代10轮后有效信息增量下降55%，仅插入一轮外部验证即可恢复迭代收益

**最值得记住的结论**：没有外部验证信号就没有可靠的自我改进，纯封闭自优化的默认结果是退化而非持续提升
