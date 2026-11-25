---
title: Provably Near-Optimal PQ in the Extended Zador Model
title_zh: 扩展Zador模型下可证明近似最优的乘积量化算法
authors:
- Edo Liberty
- Ashwin Padaki
- Amir Ingber
affiliations:
- Pinecone
- Google
- University of Pennsylvania (UPenn)
arxiv_id: '2611.31579'
url: https://arxiv.org/abs/2611.31579
pdf_url: https://arxiv.org/pdf/2611.31579
published: '2026-11-23'
collected: '2026-11-25'
category: RecSys
direction: 乘积量化 · ANN召回底层优化
tags:
- Product Quantization
- ANN Search
- Vector Database
- Embedding Compression
- KV Cache Compression
one_liner: 提出带理论保证的EZPQ乘积量化算法，精度匹敌OPQ同时提供实例级最优性证书
practical_value: '- 现有PQ流程可直接用SVD替换随机旋转作为预条件，已被证明是高斯数据下的最优选择，可直接提升量化精度

  - 若需压缩embedding、KV cache或向量数据库存储，可直接用EZPQ替换原有PQ，相同召回精度下重建MSE降低25%~78%，低比特场景下模型体积比OPQ小39%~62%

  - 低比特量化调优时可复用EZ失真估计器，比传统RWF、Zador-Gersho的估计误差低一个数量级，能更精准预判量化精度损失

  - 向量分段可复用LPT+局部搜索的bin packing策略，能将分段带来的精度损失控制在0.1%以内，远优于固定宽度分段'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有乘积量化（PQ）方法分为两类：随机旋转类无模型算法压缩率偏低，OPQ等启发式数据依赖算法缺乏理论最优性保证，且低比特、低维度场景下传统失真估计器误差大，无法给量化结果提供可信度证书，限制了其在对精度要求高的检索、KV缓存压缩场景的应用。
### 方法关键点
- 理论证明SVD是高斯数据下PQ的最优预条件旋转，随机旋转反而接近最差预条件
- 提出Extended Zador（EZ）失真估计器，结合反向注水动态比特分配和Zador-Gersho有限维空间填充惩罚，低比特低维场景下估计MAPE仅0.51%
- 将PQ分段问题转化为1维比特装箱问题，用LPT（最长处理时间优先）+局部搜索做装箱，仅引入二阶精度损失
- EZPQ编解码逻辑和传统PQ完全兼容，无需修改现有推理链路
### 关键结果
在VQ-bench的10个公开embedding数据集（维度128~1024）上对比15种基线量化方法：
- ≤2bit/坐标场景下，EZPQ精度距理论下界仅高0.7%以内，4bit场景下高3%以内
- 相比传统PQ，重建MSE降低25%~78%，精度匹敌OPQ的同时，0.5bit场景下模型体积比OPQ小39%~62%，编码速度和PQ差距在30%以内
- 即使非PQ类基线多占0.75bit/坐标的额外存储开销，EZPQ的重建MSE仍更低

**最值得记住的一句话**：做乘积量化优先用SVD预旋转，低比特场景下EZPQ是兼顾精度、效率和理论保证的最优选择之一
