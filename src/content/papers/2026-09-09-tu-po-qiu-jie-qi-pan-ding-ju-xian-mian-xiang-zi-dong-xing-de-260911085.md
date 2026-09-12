---
title: 'Beyond Solver Verdicts: Generative Reward Models for Autoformalization'
title_zh: 突破求解器判定局限：面向自动形式化的生成式奖励模型
authors:
- Vikash Singh
- Debargha Ganguly
- Aman Goel
- Ali Torkamani
- Xiaoxue Han
- Joseph Lilien
- Ferhat Erata
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
- Amazon Web Services
arxiv_id: '2609.11085'
url: https://arxiv.org/abs/2609.11085
pdf_url: https://arxiv.org/pdf/2609.11085
published: '2026-09-09'
collected: '2026-09-12'
category: Agent
direction: Agent 推理正确性验证与奖励模型优化
tags:
- Reward Model
- Neurosymbolic
- Agent Reasoning
- Autoformalization
- Verification
one_liner: 提出生成式验证方法GenV，解决神经符号系统的VPU判定欺骗问题，提升Agent推理准确率
practical_value: '- 可复用GenV的奖励模型蒸馏思路，将外部工具（如商品合规校验、库存计算工具）的判定能力蒸馏成LLM原生的连续评分，无需额外调用工具即可快速校验Agent生成的运营规则、促销逻辑的正确性

  - 针对Agent执行链中「工具返回正确但实际输入指令错误」的隐蔽漏洞，可参考VPU错误的定义设计对应检测逻辑，降低推荐/营销Agent的决策错误率

  - 测试时计算分配的优化思路可迁移到大模型推荐的推理调度场景，根据GenV类校验模型的输出动态分配计算资源，平衡推理效果与成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
神经符号系统依赖数学求解器保证推理正确性，但存在Verdict-Preserving-Unfaithfulness（VPU）漏洞：错误的形式化编码仍能成功执行并返回符合预期的判定，理论证明仅依赖求解器返回结果的校验方法对这类漏洞的检测能力仅为随机水平。

### 方法关键点
提出Generative Verification（GenV）方案，将离线Z3等价性判定的能力蒸馏为无参考的连续等价性评分，直接复用LLM原生词汇空间实现生成式校验，无需额外定位训练即可精准识别错误位置。

### 关键结果
GenV+HN版本在等价性验证任务上AUROC达0.961，可零样本泛化到未见过的翻译器与不同形式化风格，还能让Agent测试时计算分配的下游准确率提升11.3个百分点。
