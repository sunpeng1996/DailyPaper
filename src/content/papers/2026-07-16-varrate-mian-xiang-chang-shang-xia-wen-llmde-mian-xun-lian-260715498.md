---
title: 'VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context
  LLMs'
title_zh: VarRate：面向长上下文LLM的免训练可变速率KV缓存压缩
authors:
- Shahrzad Esmat
- Dhawal Shah
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2607.15498'
url: https://arxiv.org/abs/2607.15498
pdf_url: https://arxiv.org/pdf/2607.15498
published: '2026-07-16'
collected: '2026-07-20'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- LLM inference
- low-rank compression
- training-free
- long context
one_liner: 提出免训练可变速率KV缓存压缩方案，跨query复用场景精度损失远低于主流token选择法
practical_value: '- 长上下文RAG/智能客服/商品文案生成等LLM服务可直接复用VarRate方案，5倍KV压缩下精度损失不到1个点，跨query复用场景比传统token
  eviction方法少掉近10个点，无需训练改模型，落地成本极低

  - 可借鉴「分配而非驱逐」的优化思路，在推荐系统用户行为序列缓存、召回队列优化中，对低重要性item做低精度存储而非直接丢弃，避免召回遗漏、冷启动效果下降

  - 其water-filling资源分配逻辑可复用在多任务模型显存分配、电商搜索推荐流量配额分配场景，给高优先级任务/流量分配更多资源，低优先级保留最低配额，最大化整体效率

  - VarRate与量化正交，低秩压缩+3bit系数量化可把KV缓存压到原大小的9%，精度损失可忽略，适合高并发LLM接口的成本优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
KV cache是长上下文LLM推理的核心内存瓶颈，现有两类免训练压缩方案存在结构性缺陷：token选择法依赖当前query打分驱逐低重要性token，跨query复用场景下信号失效导致精度暴跌11~15个点；均匀低秩编码给所有token分配相同秩预算，在低重要性token上浪费资源、高重要性token上精度不足。

### 方法关键点
- 离线仅用少量无标注上下文对每层残差做SVD得到共享低秩基，无需训练、微调或修改模型结构
- 将KV逆RoPE旋转后拼接为每token联合向量，保留跨步锚点和最近窗口token为全精度，其余token用残差编码
- 复用SnapKV的query salience打分，通过water-filling算法给每个编码token分配可变秩，设置最低秩阈值保证无token被驱逐，总预算与均匀低秩编码完全一致
- 编码token按对应秩重建后恢复RoPE旋转，可与量化方案正交叠加

### 关键结果
在LongBench 16任务上测试Llama-3.1-8B、Qwen2.5-7B：20% KV预算（5倍压缩）下精度仅比未压缩模型低0.3/0.8个点，为同内存下最优压缩方案；跨query复用场景下仅掉点3.5~5.5，远低于token选择法的11~15个点；对比专门适配跨query复用的KVzip，精度差不到1个点，预填充开销仅为其1/8；搭配3bit系数量化可将KV缓存压缩至原大小的9%，精度损失可忽略。

### 核心结论
鲁棒性不需要靠昂贵的高质量信号实现，让廉价的错误信号拥有可恢复的容错空间（不做不可逆驱逐，仅做分级降精度），也能达到接近最优的效果。
