---
title: Looped Language Models Improve Compositional Tool Calling
title_zh: 循环语言模型提升组合式工具调用能力研究
authors:
- Andrei Cristian Popescu
- Haitz Sáez de Ocáriz Borde
- Pietro Liò
affiliations:
- University of Cambridge
arxiv_id: '2608.18171'
url: https://arxiv.org/abs/2608.18171
pdf_url: https://arxiv.org/pdf/2608.18171
published: '2026-08-16'
collected: '2026-08-20'
category: Agent
direction: Agent 工具调用 · 循环语言模型
tags:
- Looped-LLM
- Tool-Calling
- Agent
- SFT
- Adaptive-Inference
one_liner: 验证循环语言模型在组合式工具调用场景的性能优势，提出自适应推理效率优化方案
practical_value: '- 电商智能导购、广告投放决策Agent的多工具调度场景，可优先选用循环LLM架构：同参数下多步依赖工具调用Win Rate最高比普通Transformer高20%以上，小参数循环模型甚至可超过更大参数的非循环基座

  - 线上Agent服务的推理效率优化可直接复用自适应退出机制：按token粒度动态分配循环迭代次数，相比固定深度推理可降低30%左右的算力消耗，同时性能持平或略优，完美平衡延迟和效果

  - 现有工具调用LLM的低成本优化可尝试循环改造方案：无需重新预训练，基于现有基座用LoRA在Hermes这类工具调用数据集上SFT即可，改造后的模型在组合式工具调用场景可获得10%+的准确率提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM作为Agent决策核心时，在需要多API组合、跨调用依赖的复杂场景下准确率偏低；普通Transformer依赖单次前向传播生成结果，难以维护中间状态、追踪多步决策的依赖关系。循环LLM通过迭代优化隐层表征提升推理能力的机制已被验证，但在工具调用场景的价值尚未被系统探索，同时推理成本与性能的平衡问题也缺乏落地性方案。

### 方法关键点
- 对比两类循环模型：原生循环架构Ouro（1.4B/2.6B）、基于普通Transformer改造的循环版本（Llama-3.2-1B、OLMo-2-1B），所有模型采用完全相同的SFT配置（Hermes工具调用数据集、LoRA rank32、2轮训练）保证对比公平性
- 推理支持两种模式：固定循环深度推理、基于预训练停止门的自适应推理（按token粒度动态决定循环次数）
- 评测覆盖三类工具调用场景：单API调用（API-Bank）、多独立API调用（BFCL）、多步依赖API调用（NESTful）

### 关键结果
- 组合式工具调用场景收益最高：BFCL多并行调用任务上，Ouro-2.6B SFT准确率达79.75%，远超同参非循环Qwen3-4B SFT的4%；改造的Llama-3.2-1B循环版整体准确率比原生版高11.5pct。NESTful任务上Ouro-2.6B Win Rate达37.1%，超过8B参数的Qwen3-8B Instruct的34.5%
- 单API调用场景收益有限，不同模型提升幅度差异小于5pct
- 自适应推理比最优固定深度推理平均减少30%的循环次数，性能持平甚至略优，算力效率大幅提升

**最值得记住的结论**：循环LLM的迭代计算主要优化多步依赖的结构化决策能力，仅在需要多工具协同的Agent场景投入才有高ROI
