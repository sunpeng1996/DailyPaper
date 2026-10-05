---
title: 'FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution'
title_zh: FrugalEvo：成本感知的LLM引导程序进化框架
authors:
- Hui Chen
- Xuan Qi
- James Xu Zhao
- Zhaopeng Feng
- Shilong Liu
- Kuang Xu
- Pang Wei Koh
- Bryan Hooi
affiliations:
- National University of Singapore
- University of Washington
- Princeton University
- Stanford University
arxiv_id: '2610.03675'
url: https://arxiv.org/abs/2610.03675
pdf_url: https://arxiv.org/pdf/2610.03675
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 成本优化 · LLM 分工进化
tags:
- LLM Agent
- Evolutionary Search
- Cost Efficiency
- KV Cache
- Program Optimization
one_liner: 通过高低成本LLM分工、KV缓存优化实现成本感知的程序进化，同等预算下性能超SOTA
practical_value: '- 可复用高低成本LLM分工架构：在推荐策略迭代、广告文案进化、搜索排序规则优化等场景，用强LLM做策略方向探索，低成本小模型/量化模型做策略落地、代码实现、细节迭代，最高可降90%以上的LLM调用成本

  - 缓存友好的prompt构造技巧：固定公共前缀（任务规则、历史优秀方案等），高频变化内容放prompt末尾，最大化KV缓存复用，可降低30%+的API token成本与推理延迟，适合所有LLM调用场景

  - BA-AUC成本收益评估指标：可迁移用来评估Agent、生成式推荐等系统的投入产出比，替代仅看最终效果的评估方式，优化预算分配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM引导的进化算法仅优化固定迭代次数下的效果，忽略了实际业务中LLM API调用、GPU算力的成本约束，高调用成本导致这类方法难以落地到搜索推荐策略迭代、广告文案进化等真实场景。
### 方法关键点
- 架构拆分：将进化流程拆为策略探索、代码实现两个阶段，分别由高成本强LLM、低成本弱LLM承担，前者输出可落地的优化策略方向，后者完成代码编写、迭代调试
- 缓存优化：prompt构造时将固定公共内容（任务规则、历史最优方案等）放在前缀，动态变化内容（当前迭代反馈、新策略等）放在末尾，最大化KV缓存复用率
- 流程优化：新增冷启动阶段先用低成本LLM快速迭代初始方案，再进入正式进化；迭代时保留连续失败反馈，提升弱LLM调试成功率
### 关键结果
在20个数学、系统、算法优化任务上对比OpenEvolve、ShinkaEvolve等5个SOTA基线：1）10个数学与系统优化任务中9个BA-AUC更高，最终效果匹配或超过SOTA；2）圆排列任务上仅用0.55美元达到SOTA效果，比平均成本50美元的多智能体方法成本降低98%以上；3）单迭代平均成本比基线低50%以上。

最值得记住的一句话：LLM驱动的迭代类任务，通过能力匹配的模型分工、缓存优化，可在不损失效果的前提下实现数量级的成本降低
