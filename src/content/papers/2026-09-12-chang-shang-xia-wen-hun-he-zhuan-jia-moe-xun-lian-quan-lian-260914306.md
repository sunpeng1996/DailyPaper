---
title: Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training
title_zh: 长上下文混合专家（MoE）训练全链路显存峰值优化方案
authors:
- Shrey Pandit
- Xuan-Phi Nguyen
- Yiran Zhao
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.14306'
url: https://arxiv.org/abs/2609.14306
pdf_url: https://arxiv.org/pdf/2609.14306
published: '2026-09-12'
collected: '2026-09-17'
category: Training
direction: 大模型训练 · MoE长上下文显存优化
tags:
- MoE
- long-context training
- memory optimization
- distributed training
- GPU optimization
one_liner: 提出4个精度无损的流式优化算子，将MoE长上下文训练长度提升8-32倍，吞吐量最高提10.4倍
practical_value: '- 训垂直领域MoE（如生成式推荐多专家模型、Agent专用大模型）时可直接复用PipelinedLLEP，解决路由倾斜导致的OOM问题，无需修改路由逻辑、无精度损失

  - Ring-DTP可直接集成到大词表生成任务（如搜索Query生成、商品文案生成）的训练框架，词表投影层显存降86.6%，额外耗时不足5%

  - SCO+OffloadStreamAdamW组合适合中小团队用有限GPU训大模型，将显存瓶颈转移到主机内存的同时，将CPU offload优化器速度提升2.05倍

  - 四个算子可独立启用，无需全栈替换训练框架，哪类显存峰值溢出就开对应优化，渐进式集成风险极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE训练的并行方案仅能消减部分显存峰值，长上下文/大batch场景下，专家调度、词表投影、梯度检查点边界、优化器状态四类峰值随配置动态增长，任意一类超出GPU显存阈值就会触发OOM；仅优化单类峰值毫无意义，瓶颈会立刻转移到下一个未被约束的峰值，必须同时对所有峰值做确定性上限约束，且不能损失训练精度。
### 方法关键点
- PipelinedLLEP：将专家调度的batch拆为固定大小的步幅分块，限制单源节点单块发送的token数，嵌套重入梯度检查点及时释放中间张量，路由峰值上限与路由分布无关
- Ring-DTP：词表投影采用环形通信，分块计算logit并在线聚合log-sum-exp，全程不生成全量N×V的logit张量，适配大词表、长上下文场景
- SCO：选择性将梯度检查点的边界张量异步卸载到CPU内存，反向传播时提前一层预取，显存占用随主机内存预算单调下降
- OffloadStreamAdamW：将CPU offload的AdamW更新拆分为桶流水线，利用空闲GPU执行更新操作，通信计算重叠，降低offload带来的速度损失
四类算子均仅调整计算与数据移动的顺序、粒度，完全不改变模型、优化器逻辑，训练精度无损失，且可单独启用。
### 关键结果
单算子测试：PipelinedLLEP降调度峰值59.3%无速度损失，Ring-DTP降词表投影峰值86.6%耗时增<5%，SCO降显存17.7%吞吐量损失<2%，OffloadStreamAdamW提优化器速度2.05倍。
端到端测试：120B/241B/667B MoE模型上，对比调优后的FSDP2基线，最长支持1M上下文（是基线的8-32倍），吞吐量最高提10.4倍，最大全局batch最高为基线的12倍。
最值得记住的一句话：MoE长上下文训练的瓶颈从来不是平均显存占用，而是任意一个动态增长的峰值，只有实现全链路峰值的确定性绑定，才能做到训练配置的事前可预估。
