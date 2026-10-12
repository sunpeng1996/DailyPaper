---
title: 'Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers'
title_zh: Orthros：面向高效Transformer的阶段感知异构注意力机制
authors:
- Yuhong Chou
- Zehao Liu
- Yuqi Pan
- Qian Liu
- Xianwei Chen
- Zhongzhu Zhou
- Jibin Wu
affiliations:
- The Hong Kong Polytechnic University
- University of Chinese Academy of Sciences
- University of Sydney
arxiv_id: '2610.13735'
url: https://arxiv.org/abs/2610.13735
pdf_url: https://arxiv.org/pdf/2610.13735
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM高效架构 · 长上下文注意力优化
tags:
- Efficient-Transformer
- Long-Context
- Attention-Mechanism
- Prefilling-Optimization
- Inference-Acceleration
one_liner: 提出阶段感知异构注意力Orthros，实现长上下文线性预填充且无损全局召回能力
practical_value: '- 长上下文Agent/生成式推荐场景可直接复用Orthros的阶段拆分设计：prefill阶段用滑动窗口降复杂度，解码阶段用全注意力保召回，解决长用户行为序列/多轮对话的推理延迟瓶颈

  - 现有LLM4Rec底座模型可通过替换注意力为Orthros+80B token量级持续训练完成迁移，实验显示转换后性能不降反升，无需从零预训练，大幅降低改造成本

  - 推荐系统长序列召回/多轮Query理解场景，可参考其滑动窗口+全注意力异构设计，平衡计算效率与长程依赖召回准确率

  - 推理引擎优化时可复用其训练推理一致的设计逻辑，避免架构改动带来的对齐成本，适配SGLang等主流推理框架，快速落地性能增益'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有线性、滑动窗口等高效注意力机制存在长上下文召回退化问题，混合架构仍受全注意力层的二次复杂度瓶颈限制，无法适配Agent多轮对话、生成式推荐长用户行为序列等「重prefill、轻解码」的主流长上下文工业场景。
### 方法关键点
- 核心思路将复杂度分配从结构维度转向阶段维度，统一注意力模块内动态切换计算模式：prefill阶段采用滑动窗口注意力实现线性复杂度，解码阶段额外叠加全跨注意力保证全局召回能力
- 训练推理严格对齐，仅通过调整上下文长度Tin、输出长度Tout参数，即可无缝适配预训练、SFT、prefill、解码四类场景，无需修改上层架构
- 支持现有Transformer底座低成本迁移：仅替换原生注意力模块，经少量数据持续训练即可完成转换，无需从零预训练
### 关键实验结果
- 对比Llama3.1-8B、Qwen3-8B基线，转换后的Orthros模型在常识推理、MMLU基准上平均性能提升1~2pp，128K大海捞针任务召回准确率接近100%
- 1M token超长长上下文下，prefill速度较vanilla Transformer提升21.9×，端到端推理延迟降低70%以上，解码阶段额外开销完全被I/O瓶颈掩盖，吞吐量与基线持平
### 核心结论
对于prefill远重于解码的主流工业长上下文场景，阶段异构的注意力拆分设计可在完全无损召回能力的前提下实现数量级推理效率提升
