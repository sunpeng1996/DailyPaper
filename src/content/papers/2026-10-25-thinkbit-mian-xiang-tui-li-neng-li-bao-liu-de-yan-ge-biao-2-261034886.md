---
title: 'ThinkBit: Search Codewords, Recalibrate Scales, Select by Reasoning'
title_zh: ThinkBit：面向推理能力保留的严格标量2-bit大模型量化框架
authors:
- Rhea Sanjay Sukthanker
- Pashmina Cameron
affiliations:
- Microsoft Applied Sciences Group
arxiv_id: '2610.34886'
url: https://arxiv.org/abs/2610.34886
pdf_url: https://arxiv.org/pdf/2610.34886
published: '2026-10-25'
collected: '2026-10-28'
category: LLM
direction: 大模型量化 · 推理能力保留
tags:
- LLM-Quantization
- 2-bit-Quantization
- Reasoning-LLM
- QAT
- Scalar-Quantization
one_liner: 提出5阶段严格标量2-bit量化框架，体积降8倍的同时大幅保留大模型长链推理能力
practical_value: '- 端侧部署LLM4Rec、导购Agent等低资源场景时，可直接复用该2-bit量化框架，在体积降低8倍的同时保留多轮推理、推荐理由生成等长逻辑能力，大幅降低端侧部署成本

  - 低比特LLM选型时，不要仅依赖perplexity、通用问答准确率等指标，必须加入业务场景专属的长推理链路测试（如电商多轮导购决策、搜索query多意图拆解验证），避免指标虚高但实际推理逻辑失效

  - 量化优化pipeline可直接复用「分层灵敏度分配位宽→冻结码本校准scale→短QAT+业务推理测试选checkpoint」的流程，在不增加太多训练成本的前提下平衡压缩率和业务效果

  - 针对电商/推荐专属场景的量化模型，可在QAT阶段加入业务推理轨迹数据微调，能大幅提升场景推理准确率，且通用指标损失极小'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
推理类LLM生成长链思考内容时，内存带宽是推理速度的核心瓶颈，2-bit量化相比bf16可降低8倍内存占用与访存开销，但现有2-bit量化方法普遍依赖perplexity、选择题准确率等指标评估，无法反映长链推理能力的真实损失，且多数非严格标量格式部署复杂度高，亟需兼顾推理能力保留、部署友好的2-bit量化方案。
### 方法关键点
- 采用严格标量权重格式：每个存储权重为整数码本乘以每组128个权重共享的bf16 scale，无向量码本、旋转、零点，反量化仅需一次乘法，部署难度极低
- 5阶段量化流程：1）用KronQ二阶灵敏度指标为每层分配三元/2-bit/3-bit位宽，最优分配位宽预算；2）基于Gumbel-softmax/ReinMax松弛的块级码本搜索，逐Transformer block优化初始码本；3）冻结码本，仅校准scale和RMSNorm增益，通过KL散度蒸馏对齐bf16模型输出分布；4）短QAT阶段微调少量码本，加入隐状态蒸馏损失；5）用MATH训练集的配对推理测试，从校准和QAT两个checkpoint中选择推理表现更优的版本
### 关键结果
核心推理指标采用MATH-500、AIME@16，对比基线覆盖EfficientQAT、BitDistiller、主流GGUF 2-bit版本、Bonsai量化方案：
- Qwen3-1.7B 0.52GB版本（2.42bit/参）MATH-500采样准确率达73.0，同尺寸下EfficientQAT仅30.0，比所有公开2-bit GGUF版本更小且推理准确率更高
- Qwen3-14B 3.74GB版本MATH-500准确率达94.8，仅比29.5GB的bf16版本低2.7个点，单卡batch1推理速度提升74%
> 最值得记住的结论：常规大模型量化评估指标（perplexity、通用QA准确率）无法反映长推理能力的损失，低比特推理类模型必须用真实推理链路任务做选型和效果验证。
