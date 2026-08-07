---
title: Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard
  Documents
title_zh: 面向国标文档规则密集审核的LLM基准构建与多智能体增强方法
authors:
- Tao Wang
- Qihao Yang
- Rongjiao Liang
- Lianghong Lin
- Haitao Wang
- Xinyu Cao
- Tianyong Hao
affiliations:
- South China Normal University
- Shanghai Jiao Tong University
- China National Institute of Standardization
arxiv_id: '2608.06312'
url: https://arxiv.org/abs/2608.06312
pdf_url: https://arxiv.org/pdf/2608.06312
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 多智能体协作 · 规则密集长文档审核
tags:
- Multi-Agent
- Long Document Processing
- Benchmark
- Rule-intensive Review
- LLM Evaluation
one_liner: 提出首个国标审核基准GB/T-Bench与多智能体框架，将最优模型CMCS从0.328提升至0.5094
practical_value: '- 做电商合规文案审核、广告素材合规校验、平台规则一致性巡检等规则密集类审核任务时，可复用「全局扫描+维度专家+细粒度错误Agent+规则扫描」的分层多智能体架构，相比单prompt效果提升显著

  - 构建专业领域基准数据集时，可采用「确定性规则注入错误+约束LLM改写生成反例」的方法，大幅降低标注成本，同时保证错误可追溯

  - 长文档多智能体系统设计中需优先保障全局上下文理解模块，缺失全局扫描的细分Agent推理会产生碎片化问题，效果甚至低于单prompt基线

  - 多错误诊断类业务的效果评估可复用CMCS指标，同时兼顾错误覆盖率、漏检惩罚和误报惩罚，比单纯Recall更贴合业务对精度和召回的平衡要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM在规则密集型专业文档审核场景的能力缺乏系统评估，国标（GB/T）文档审核需要严格遵循结构、术语、规范性表述等多维度规则，当前完全依赖人工审核成本高、周期长，现有基准多聚焦领域知识问答，缺少针对文档本身质量审核的诊断级评估体系，无法支撑LLM在该类高风险场景的落地。

### 方法关键点
- 构建GB/T-Bench：首次提出覆盖5个审核维度、25种细粒度错误类型的国标审核分类体系，通过确定性规则+约束LLM改写的可控反例生成机制，基于488份国标文档生成7306条可追溯错误实例，配套诊断级评估协议，要求预测的错误位置、维度、类型三者完全匹配才算正确。
- 提出GB/T-Reviewer多智能体框架：分为文档解析、专家审核、预测融合三个模块，专家层集成全局扫描Agent、维度专属专家Agent、细粒度错误类型Agent、规则扫描器四类组件，输出候选错误后经过滤、去重、融合得到结构化审核结果。

### 关键实验结果
在14款主流LLM上测试，单prompt模式下最优模型（GPT-5.6-sol）CMCS仅为0.328，不足人类专家（0.664）的一半；搭配GB/T-Reviewer后，最优CMCS提升至0.5094，相对提升55.3%，同时各模型的错误召回率、高阈值诊断完成率均有大幅提升。Ablation显示移除全局扫描模块后性能甚至低于单prompt基线，是架构中最核心的组件。

**最值得记住的一句话**：规则密集型长文档审核任务中，分层多智能体协作的效果显著优于单prompt大模型，全局上下文理解是细粒度诊断的基础。
