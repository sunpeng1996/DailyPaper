---
title: 'Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal
  Reasoning'
title_zh: 熵谱引导的视觉重对齐解码：捕获多模态推理动态规律
authors:
- Jiaqi Deng
- Zhe Fu
- Yakun Chen
- Dichang Zhang
- Zonghan Wu
- Xiaoshui Huang
- Huan Huo
- Guandong Xu
affiliations:
- University of Technology Sydney
- Alibaba Cloud Computing
- Stony Brook University
- East China Normal University
- Shanghai Jiao Tong University
arxiv_id: '2611.06415'
url: https://arxiv.org/abs/2611.06415
pdf_url: https://arxiv.org/pdf/2611.06415
published: '2026-11-04'
collected: '2026-11-05'
category: Multimodal
direction: 多模态大模型·幻觉抑制解码
tags:
- MLLM
- Hallucination Mitigation
- Entropy-aware Decoding
- Multimodal Reasoning
- Inference Optimization
one_liner: 免训练熵感知解码框架SEED，通过动态视觉重对齐降低MLLM推理幻觉，提升准确率
practical_value: '- 做电商多模态导购Agent、商品图文理解场景时，可复用熵动态检测逻辑，实时识别MLLM推理中的幻觉风险，避免输出与商品图不符的错误介绍

  - 无需重新训练MLLM，仅在解码层注入注意力重对齐逻辑即可降低幻觉，适合业务侧快速上线优化，额外计算开销仅5%，对推理延迟敏感的场景友好

  - 可复用「全局低熵+局部熵突增」的双条件检测规则，识别各类大模型推理的不稳定状态，拓展到纯文本CoT推理、RAG回答校验、推荐理由生成等场景'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前多模态大模型（MLLM）在长链Chain-of-Thought推理中容易出现与视觉上下文不符的幻觉，现有解决方案要么需要高成本的重新训练/微调，要么仅在token层面做静态干预，未考虑多模态信息交互的动态过程，难以适配复杂推理场景。

### 方法关键点
- 先通过大样本统计识别出两类和幻觉强相关的熵动态模式：全局持续低熵（对应模型过早收敛到错误的多模态交互模式）、局部熵突增（对应推理不稳定，幻觉即将出现）
- 免训练SEED解码框架在解码阶段实时监测每步熵值，同时满足「当前熵低于历史轨迹均值」+「单步熵涨幅超过阈值τ_rise=0.25」时触发干预
- 干预逻辑：预填充阶段从ViT最后层注意力提取视觉重要性图，聚合得到加权的视觉引导向量，在LLM第一层做残差注入，强化视觉接地，避免过度依赖语言先验

### 关键实验
基于Qwen3-VL 4B/8B、Llama-3.2-11B-Vision三个主流MLLM backbone，在6个多模态基准（含M3CoT、POPE、HallusionBench共9种评估设置）上测试，对比VCD、MemVR等SOTA免训练幻觉抑制方法，平均推理准确率提升3.15%~3.71%，幻觉抑制指标平均提升2.49%~3.56%，额外计算开销不到5%。

### 核心结论
成功的多模态推理不需要最大化模型置信度，反而需要在生成过程中维持可控的不确定性，保证视觉信息被有效整合到推理链路中。
