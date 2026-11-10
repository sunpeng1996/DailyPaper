---
title: MNN-Pocket-0.3B Technical Report
title_zh: MNN-Pocket-0.3B端侧轻量大模型技术报告
authors:
- MNN Team
affiliations:
- Taobao and Tmall Group of Alibaba
arxiv_id: '2611.12311'
url: https://arxiv.org/abs/2611.12311
pdf_url: https://arxiv.org/pdf/2611.12311
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: 端侧轻量LLM 全链路协同优化
tags:
- On-device LLM
- Quantization
- Knowledge Distillation
- Inference Optimization
- Tiny LLM
one_liner: 推出300M参数支持32K上下文的端侧大模型，INT4体积仅173MB，性能超同规模及部分0.5B模型
practical_value: '- 业务端侧场景可直接复用该模型：电商端侧UGC评论分析、端侧推荐触发、端侧Agent交互等场景，相比云端方案降本70%以上，同时保护用户隐私

  - 小模型训练可复用多教师On-Policy Distillation + QAT方案：量化后性能损失<0.5%，可在300M参数量下同时覆盖知识、指令遵循、代码、数学能力

  - 端侧推理优化方案可直接迁移：MNN的phase-aware低比特核、硬件定制KV cache、speculative decoding优化，最高可将端侧解码速度提升1.65倍

  - 电商UGC理解场景实测：该模型LoRA微调后做评论观点挖掘F1达80.15，比Qwen3-1.7B高1.56分，参数量仅为其1/5，适合低资源部署'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端侧智能在搜索推荐、短视频、XR等场景已落地产生价值，但现有小参数量LLM无法同时平衡内存占用、推理速度和多任务性能，难以满足消费级应用200-300MB驻留内存、200tok/s以上解码速度的硬约束，亟需端侧优先的全链路协同优化方案。
### 方法关键点
- 硬件感知架构+Tokenizer协同设计：选定300M参数28层GQA架构，依赖感知裁剪Tokenizer词表从151K压缩到64K，平衡序列压缩率和嵌入层内存开销
- 四阶段预训练：基于4.1T高质量中英、数学、代码数据，按质量、知识密度、难度分桶动态调度，在小参数量约束下最大化知识获取效率
- 三阶段后训练：SFT循环引擎迭代补全能力缺口，多教师On-Policy Distillation（MOPD）融合知识、指令遵循、数学、代码4个领域专家能力，Self-OPD+QAT将INT4量化性能损失控制在0.5%以内
- MNN推理引擎协同优化：phase-aware低比特核、融合Transformer算子、硬件定制KV cache实现高效INT4推理，可选speculative decoding进一步提升解码速度
### 关键结果
11项基准测试平均得分50，超同规模最优基线18分，甚至超过部分0.5B参数模型；INT4量化后体积仅173MB，iPad Pro M5上解码速度达466tok/s，骁龙8 Gen5上达251tok/s，加speculative decoding平均提效1.15-1.65倍；电商场景实测，LoRA微调后做评论观点挖掘F1达80.15，比Qwen3-1.7B高1.56分，参数量仅为其1/5。
> 最值得记住的一句话：端侧小模型的性能瓶颈从来不只在参数量，架构、数据、训练、推理的全链路协同优化才是兼顾效果和效率的核心
