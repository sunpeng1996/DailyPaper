---
title: 'Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction
  Conflict, Embedded Commands, and Policy Ambiguity'
title_zh: 对抗语用学AI安全评估：指令冲突、嵌入命令与政策模糊性基准
authors:
- Brett Reynolds
affiliations:
- Humber Polytechnic
- University of Toronto
arxiv_id: '2607.01153'
url: https://arxiv.org/abs/2607.01153
pdf_url: https://arxiv.org/pdf/2607.01153
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: LLM安全评估 · 对抗语用学标注体系
tags:
- AI Safety Evaluation
- LLM Judge
- Prompt Injection
- Annotation Protocol
- Benchmark
one_liner: 提出基于对抗语用学的LLM安全评估基准与标注协议，细粒度区分安全失败根因
practical_value: '- 业务Agent/LLM安全评估可抛弃单一pass/fail标签，拆分任务成功、政策合规、安全风险、拒答结果多维度打标，精准定位故障根因

  - 构造prompt注入攻击测试集时，可复用论文覆盖的指令冲突、嵌入命令、指代模糊等语用层攻击场景，提升防御测试的全面性

  - 用LLM Judge做业务自动判分（如生成式推荐文案合规性校验、Agent执行结果打分）时，可参考评估者信度、标注歧义度等度量方法，提升判分稳定性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM安全评估多采用pass/fail二分类标签，无法区分安全失败是来自能力不足、政策模糊、指令冲突、框架故障还是评估者判断不稳定，难以定位根因。
### 方法关键点
1. 构建基于语言学的对抗语用学评估分类体系，覆盖指令冲突、嵌入命令、引用、范围歧义、指示语、间接言语行为、多轮Agent会话7类场景
2. 产出18条种子基准样例、54条本地试点数据集，配套专家标注协议，拆分任务成功、政策合规、安全风险、拒答结果、评估者置信度5类标注维度
3. 设计评估者信度、诊断歧义度、分类漂移三类度量指标，量化评估流程稳定性
### 关键结果
该框架可直接复用于安全评估校验、LLM Judge优化、金标准数据集构建、Prompt Injection测试、安全文档生成等场景
