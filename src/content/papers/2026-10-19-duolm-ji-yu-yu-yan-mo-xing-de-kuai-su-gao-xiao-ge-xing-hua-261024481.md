---
title: 'DuoLM: Fast and Effective Personalized Recommendation with Language Models'
title_zh: DuoLM：基于语言模型的快速高效个性化推荐框架
authors:
- Jiang Wu
- Yutong Song
- Hongbo Wang
- Guanghe Cao
- Jeff Lei Liang
affiliations:
- Independent Researcher
- University of California, Irvine
- Google DeepMind
- Oracle
arxiv_id: '2610.24481'
url: https://arxiv.org/abs/2610.24481
pdf_url: https://arxiv.org/pdf/2610.24481
published: '2026-10-19'
collected: '2026-10-26'
category: RecSys
direction: LLM驱动个性化推荐 · 推理性能优化
tags:
- LLM4Rec
- Knowledge Distillation
- KV Cache
- CUDA Graph
- Inference Optimization
one_liner: 双LLM蒸馏训练搭配定制化推理优化，在无损推荐效果前提下吞吐量最高提109倍
practical_value: '- 模型侧可复用「编码器LLM离线生成全局item向量+轻量化排序LLM在线打分」架构，配合知识蒸馏对齐full-text大模型效果，同时兼顾冷启动泛化性和在线性能，适配电商大候选集排序场景

  - 推理侧可直接落地3个优化trick：用Virtual Token ID映射GPU驻留item向量表，减少90%+请求传输开销；多候选共享用户历史KV缓存，单请求多候选打分避免重复计算；CUDA
  Graph replay减少CPU调度开销，可额外提1~3.5倍吞吐量

  - 训练策略优先选择「CE排序损失+KL蒸馏损失」联合训练，蒸馏权重β线性升温到0.5左右，相比纯监督训练NDCG@10可提升约2%，无需额外加自对齐损失（会增加训练成本且效果下降）

  - 若无需将用户反馈编码到item向量，优先选择将反馈输入排序器的FIR方案，item向量可全局复用，推荐效果优于将反馈编码进item的FIE方案'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM落地个性化推荐面临两大核心痛点：一是全文本cross-encoder在线计算量过大，item表征无法跨用户复用，吞吐量极低；二是模型计算量优化无法直接转化为端到端性能提升，用户历史重复计算、CPU调度开销等会进一步限制服务性能，严重制约LLM推荐的业务落地。
### 方法关键点
- 模型架构：双LLM设计，编码器LLM离线将每个item的文本压缩为独立的EOS隐向量，通过RMS归一化+尺度校准接口输入给个性化排序LLM，排序器结合用户历史交互、反馈文本和候选向量输出排序分数
- 训练策略：端到端联合训练编码器和排序器，同时使用推荐任务CE损失和full-text教师模型的KL蒸馏损失对齐效果，蒸馏权重线性升温至0.5
- 推理优化：① Virtual Token ID映射GPU驻留item向量表，大幅降低请求传输量；② 多候选共享用户历史前缀KV缓存，树型注意力掩码隔离不同候选，避免重复计算历史；③ CUDA Graph replay减少CPU调度和内核启动开销
### 关键实验
在Amazon Books、Video Games数据集测评，对比full-text教师模型、HLLM、ContentSASRec等baseline：① 效果上，Books数据集NDCG@10达0.5586，超过教师模型的0.5440；Video Games数据集NDCG@10达0.5298，与教师模型的0.5313基本持平；② 性能上，单H100吞吐量达26400候选/秒，是vLLM部署教师模型的60.1倍、SGLang部署的109.9倍，p99 latency仅536.9ms（教师vLLM部署为17093.82ms）。

最值得记住的一句话：LLM落地推荐场景的核心瓶颈不在效果，而在推理性能，通过「离线预计算+在线共享计算+底层调度优化」的组合方案，可在几乎无损效果的前提下带来两个数量级的吞吐量提升。
