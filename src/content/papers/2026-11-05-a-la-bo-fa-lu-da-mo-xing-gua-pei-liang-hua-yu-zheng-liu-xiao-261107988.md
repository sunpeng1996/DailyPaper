---
title: 'Compression Through a Context Lens: Evaluating Adaptation, Quantization, and
  Distillation in Arabic Legal LLMs'
title_zh: 阿拉伯法律大模型适配、量化与蒸馏效果评估：基于上下文视角的压缩研究
authors:
- Md. Rafiul Biswas
- George Mikros
- Wajdi Zaghouani
affiliations:
- Hamad Bin Khalifa University
- Northwestern University in Qatar
arxiv_id: '2611.07988'
url: https://arxiv.org/abs/2611.07988
pdf_url: https://arxiv.org/pdf/2611.07988
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 大模型压缩 · 双协议性能评估
tags:
- LLM-Compression
- Quantization
- Knowledge-Distillation
- Domain-Adaptation
- LLM-Evaluation
one_liner: 通过有/无上下文双评估协议量化阿拉伯法律大模型适配、量化与蒸馏的性能 trade-off
practical_value: '- 压缩选型参考：4-bit NF4量化可实现64%-71%内存缩减，无上下文精度损失仅±3.2pp，优先选NF4而非FP4，适合端侧Agent/轻量化生成式推荐模型部署

  - 评估方法借鉴：在RAG/生成式推荐场景，需同时做有上下文（RAG召回结果输入）和无上下文（模型自身参数知识）的双维度评估，避免高估带外部输入时的实际能力

  - 蒸馏策略参考：跨架构硬标签蒸馏可实现接近教师的性能，同架构蒸馏时学生参数量不低于教师的40%时精度损失可控，适合小尺寸垂域LLM的低成本训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
域内大模型部署常受资源限制，现有压缩效果评估多以通用/英文基准为主，且通常仅测试带上下文输入的性能，无法区分模型是依赖输入信息还是自身参数知识，低资源语言垂域的压缩表现更缺乏系统性验证。

### 方法关键点
- 双评估协议：有上下文（开卷，带领域参考文本）、无上下文（闭卷，仅输入问题），后者衡量模型参数内的知识保留度
- 三阶段实验：先做域适配（QLoRA实现CPT、SFT、CPT→SFT三种策略），再做后训练量化（INT8、INT4 NF4、INT4 FP4），最后做硬标签知识蒸馏
- 测试覆盖3款开源LLM：阿拉伯专属FANAR-9B、JAIS-8B，多语种Qwen2.5-7B

### 关键结果
基于沙特阿拉伯法律基准ARABLEGALEVAL测试：1）基础模型无上下文精度比有上下文低7.6~27pp，最高差距达27pp；2）4-bit NF4量化缩减64~71%内存，无上下文精度波动仅-3.2~+1.6pp，表现优于同位宽FP4；3）跨架构蒸馏的7B学生模型无上下文精度仅比9B教师低0.6pp，小于1.5B的学生模型精度下降显著。

最值得记住的一句话：对知识密集型垂域大模型，无上下文评估是带上下文测试的必要补充，能更准确反映压缩后的知识保留能力
