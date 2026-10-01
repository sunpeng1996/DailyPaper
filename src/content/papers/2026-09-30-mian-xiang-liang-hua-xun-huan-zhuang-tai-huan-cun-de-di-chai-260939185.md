---
title: Low-Discrepancy Dither for Quantized Recurrent State Caches
title_zh: 面向量化循环状态缓存的低差异抖动优化方法
authors:
- Snigdha Chandan Khilar
affiliations:
- Independent Researcher
arxiv_id: '2609.39185'
url: https://arxiv.org/abs/2609.39185
pdf_url: https://arxiv.org/pdf/2609.39185
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: LLM循环状态缓存量化推理优化
tags:
- Quantization
- Mamba
- State Cache
- Inference Optimization
- Low Precision
one_liner: 提出无需随机数的黄金比例Weyl抖动，性能优于Mamba类模型常用的随机取整方案
practical_value: '- 业务中若使用Mamba/混合SSM架构LLM做Agent推理、生成式推荐文案生成，可直接替换现有随机取整为Weyl抖动，无额外计算成本，可降低11%~49%的量化KL偏差，还可省掉随机数生成开销

  - 若生成序列长度普遍<2000步，就近取整（rtn）可作为低成本选项；若生成长度超过2000步（如长对话Agent、长文档摘要）必须替换为Weyl抖动，避免rtn的误差线性累积导致效果劣化

  - 实现Weyl抖动时需避开三个坑：避免使用接近简单分数的增量、offset不要与时间增量混叠、相位计算优先用双精度/整数计算，否则收益会完全消失

  - 可尝试将低差异抖动思路迁移到KV cache量化、模型权重量化场景，降低随机取整的方差，提升低精度推理效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Mamba类状态空间模型与混合SSM-Transformer架构的LLM通过固定大小的循环状态缓存实现长上下文建模，将状态低精度存储可大幅降低内存带宽开销，但循环状态的量化误差会持续反馈到后续步长累积，现有生产环境常用的随机取整（sr）误差偏高，就近取整（rtn）的误差会随生成长度线性增长，亟需更优的量化取整方案。
### 方法关键点
- 对比三类取整规则：rtn（就近取整）、sr（基于随机数的概率取整）、Weyl抖动（基于黄金比例的确定性低差异序列生成取整阈值，无需随机数）
- 理论证明三类规则的误差增长规律：rtn误差线性增长、sr误差随步长根号级增长、Weyl抖动误差仅随步长对数级增长
- 覆盖纯Mamba、混合SSM-Transformer两类架构，测试INT8、FP8、BF16三种低精度格式，最长测试4096步生成场景
### 关键实验结果
在WikiText-103、PG-19数据集上测试，对比sr、rtn baseline：
1. 15组核心实验中Weyl抖动的KL偏差全部低于sr，降幅11%~49%，中位数31%，优势可保持到4096步，等效于每个存储值多0.25bit的精度
2. rtn在生成步长<2000时可能效果最优，但步长超过2000后误差线性增长，4096步时最多比Weyl抖动差400倍
3. 明确三个实现坑点：增量接近简单分数、offset与时间增量混叠、相位用float32计算，都会完全抵消Weyl抖动的收益
### 最值得记住的一句话
低精度存储循环状态时，优先用无额外成本的Weyl抖动替代随机取整，长生成场景禁用就近取整。
