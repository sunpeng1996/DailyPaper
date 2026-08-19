---
title: Chain-of-Experience for Continual LLM Improvement
title_zh: 经验链(CoE)：大语言模型推理阶段的持续迭代优化框架
authors:
- Haoqin Tu
- Yunhao Fang
- Yizhong Wang
- Cihang Xie
- Shen Yan
affiliations:
- UC Santa Cruz
- Bytedance Seed
arxiv_id: '2608.18027'
url: https://arxiv.org/abs/2608.18027
pdf_url: https://arxiv.org/pdf/2608.18027
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: 大语言模型 · 推理阶段持续优化
tags:
- Chain-of-Experience
- Test-time Learning
- Feedback-driven Optimization
- LLM Reasoning
- Inference Efficiency
one_liner: 提出推理阶段反馈驱动的CoE框架，让LLM在不训练的情况下持续迭代提升性能并降低API成本
practical_value: '- 电商生成式文案、导购Agent等场景可直接复用CoE框架：对接用户点击/转化、代码执行、模型自评估三类反馈做迭代优化，实测可在提效的同时降低19%左右API成本

  - 避免对历史推理经验做过度压缩：实验显示Dynamic CheatSheet、SimpleMem等内存压缩方法会丢失关键信息，全量经验轨迹+反馈的效果优于压缩经验

  - 多反馈通道组合可进一步提升效果：对于商品详情页生成、代码类工具Agent任务，组合自反馈与正确性/执行反馈，可获得单路反馈之上的额外增益

  - 控制迭代轮次降低开销：大部分性能增益在前20轮即可收敛，后续迭代边际收益极低，可设置合理迭代上限减少推理耗时与成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统LLM部署后参数固定，单次推理相互孤立，无法利用任务执行过程中产生的反馈持续优化；现有自修正、经验记忆类方法要么不保留跨轮经验，要么对经验的利用碎片化，效果和效率均不理想，亟需统一的推理阶段持续优化范式。
### 方法关键点
- 定义Chain-of-Experience(CoE)范式：每轮输出依赖之前所有轮次的响应+对应反馈组成的完整经验链，无需重新训练模型，纯推理阶段即可实现迭代优化
- 覆盖四类反馈信号：无反馈、代码执行反馈（运行结果、报错信息）、模型自反馈（文本点评、偏好打分）、正确性二元反馈（是否符合要求），适配不同场景的反馈可得性
- 统一对比三类现有经验利用基线：Few-shot ICL、Dynamic CheatSheet(DC)、Agentic Context Engineering(ACE)，验证CoE的优越性
### 关键结果
在数学（AIME2025、OmniMath）、编码（LiveCodeBench V6、LiveBench Code）、知识（EvaLearn、GPQA Diamond）三类任务的8个SOTA LLM（GPT-5、Claude 4.5 Sonnet等）上测试：
- CoE+自反馈对比无反馈基线平均提升5.6%，同时API成本降低19%，效果比ICL/DC/ACE等基线高7-9个百分点
- 组合模型自反馈+正确性/执行反馈的双路模式，比单路反馈额外提升6-10个百分点
- LLM基础能力和CoE提升幅度正相关，平均Pearson系数0.5，越强的模型越能从反馈中获益

> 最值得记住：大模型推理阶段的反馈迭代优化，效果优于单纯增加推理token、导入外部经验等常规手段，是兼顾效果和成本的实用优化路径。
