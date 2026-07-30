---
title: 'GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding'
title_zh: GPTQ-2D：三次时间复杂度的双边自适应量化舍入算法
authors:
- Jiale Chen
- Torsten Hoefler
- Dan Alistarh
affiliations:
- Institute of Science and Technology Austria (ISTA)
- ETH Zürich
- Red Hat AI
arxiv_id: '2607.27042'
url: https://arxiv.org/abs/2607.27042
pdf_url: https://arxiv.org/pdf/2607.27042
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: 大模型量化 · 双边自适应舍入加速
tags:
- GPTQ
- LLM Quantization
- Adaptive Rounding
- Kronecker Product
- Efficient Inference
one_liner: 提出三次时间复杂度的双边自适应舍入算法GPTQ-2D，将双边量化时间从四次降至三次
practical_value: '- 服务端LLM部署优化：GPTQ-2D可实现低精度（2/4bit）双边量化几乎无精度损失，直接用于电商Agent、LLM排序/生成式推荐场景的部署，降低推理延迟与显存占用

  - 工程优化迁移：反对角并行计算、分块懒更新、倾斜内存布局三个核心优化可直接复用至其他矩阵运算加速场景，比如大规推荐模Embedding量化、用户/物品语义矩阵压缩

  - 现有量化流程升级：在采用Kronecker近似的量化场景下，直接替换原有舍入模块即可获得min(m,n)倍的量化速度提升，无额外适配成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有GPTQ等单边自适应舍入算法仅支持单侧二次度量下的矩阵量化，广泛应用于LLM后训练量化场景；但当引入双边基矩阵（如Kronecker分解的Hessian近似，可提升量化精度）时，直接向量化实现的时间复杂度高达O(m²n²)（四次），无法适配LLM大参数矩阵的量化需求，落地难度高。
### 方法关键点
- 利用Kronecker乘积的结构特性，证明同一反对角线上的矩阵元素舍入互不依赖，可并行计算，天然适配GPU并行架构
- 引入辅助缓冲区C=LE存储累积反馈，将原本逐元素的全块误差更新拆解为行/列两个方向的增量推送，将舍入遍历复杂度从四次降到O(mn·max(m,n))
- 提出分块懒更新和倾斜内存布局优化，解决反对角元素访问的内存带宽瓶颈，进一步提升硬件执行效率
- 理论证明GPTQ-2D的舍入结果和直接向量化实现完全等价，无精度损失，且当右基矩阵B=I时可退化为标准GPTQ，兼容现有量化流程
### 关键结果
对于m≥n的矩阵，GPTQ-2D总时间复杂度为O(m³)，和标准单边GPTQ完全一致，比直接双边量化实现快min(m,n)倍；并行阶段数为O(max(m,n))，可支持大规格矩阵的高效量化。
### 核心结论
双边自适应舍入可以通过利用Kronecker结构的反对角并行性，将时间复杂度降到和单边舍入一致，是LLM低损量化的高效落地方向。
