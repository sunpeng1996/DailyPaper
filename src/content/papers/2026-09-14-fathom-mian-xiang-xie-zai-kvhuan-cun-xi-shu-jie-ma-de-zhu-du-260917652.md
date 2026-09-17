---
title: 'Fathom: Per-Query Read Depth for Sparse Decoding over Offloaded KV Caches'
title_zh: Fathom：面向卸载KV缓存稀疏解码的逐查询读取深度优化
authors:
- Vivek Kalyanarangan
arxiv_id: '2609.17652'
url: https://arxiv.org/abs/2609.17652
pdf_url: https://arxiv.org/pdf/2609.17652
published: '2026-09-14'
collected: '2026-09-17'
category: LLM
direction: LLM长上下文推理 · KV缓存优化
tags:
- KV Cache
- Long Context LLM
- Sparse Attention
- Inference Optimization
- Quantization
one_liner: 提出逐查询动态分配KV缓存读取位宽的方法，长上下文卸载场景解码速度提升1.67倍
practical_value: '- 长会话Agent服务（如电商导购、客服）可复用位平面存储+反向水填充位宽分配方案，降低KV缓存卸载的PCIe传输开销，提升单卡并发会话数

  - KV缓存量化工程可借鉴通道优先位平面存储设计，前缀读取天然对应多精度量化器，无需额外存储多份低精度索引

  - 稀疏Attention优化可参考逐查询按通道重要性分配位宽的思路，替代固定位宽/固定通道选择方案，同精度下降低访存

  - 注意适用边界：仅KV缓存索引卸载到主机内存时收益明显，索引可放入GPU HBM时因算术开销反而无速度优势'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文Agent会话长度可达百万token，多并发场景下KV缓存无法全部放入GPU显存，只能卸载到主机内存，解码瓶颈由KV缓存索引扫描的PCIe传输带宽决定。现有稀疏attention扫描方案采用固定读取位宽，未利用不同通道对当前查询的重要性差异，带宽浪费严重。
### 方法关键点
- 4bit量化的K缓存按通道优先存储为位平面，读取前t个位平面即可得到tbit精度的量化结果，无需额外存储低精度索引副本
- 每个查询按通道的方差加权重要性，通过反向水填充算法动态分配各通道读取位宽，在总位宽预算下最小化注意力得分误差
- 带QK-norm的模型直接用原始通道，无QK-norm的模型用KLT旋转后的通道，进一步提升位宽利用效率；默认用全局平价位宽预算，固定部署场景可校准为逐层预算
### 关键结果
在7种模型+上下文配置上对比SparQ、Double Sparsity、Loki等基线：1M token场景下解码GPU时间比136bit扫描基线快1.67倍；相同GPU时间下比SparQ r=16少读18%字节，注意力误差低1.1~5.3倍；真实编码Agent会话下92bit读取即可达到136bit扫描的步级一致性。
### 核心结论
KV缓存优化的收益完全由存储层级决定：索引在主机内存时降低读取字节数就是降低耗时，索引在GPU HBM时反而要优先控制算术开销。
