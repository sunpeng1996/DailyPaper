---
title: 'Adaptive Model Compression (AMC): Saliency-Driven Resource Allocation for
  Ultra-Low-Power Transformer Inference'
title_zh: 自适应模型压缩AMC：面向超低功耗Transformer推理的显著性驱动资源分配
authors:
- Jiayin Hu
- Kai Yuan
- Vanessa Hu
- Xuetao Yin
- Jianhua Li
- Sean Suchter
affiliations:
- Apple USA
arxiv_id: '2607.10109'
url: https://arxiv.org/abs/2607.10109
pdf_url: https://arxiv.org/pdf/2607.10109
published: '2026-07-11'
collected: '2026-07-14'
category: LLM
direction: LLM推理优化 · 动态压缩 软硬件协同
tags:
- Model Compression
- Transformer Inference
- Edge AI
- Hardware-Software Co-design
- Low Power Computing
one_liner: 提出显著性驱动的软硬件协同Transformer动态压缩框架，实现边缘端超低功耗推理
practical_value: '- 端侧电商导购Agent、生成式推荐场景可直接复用KV cache分级压缩思路：对KV token按显著性打分，非 salient
  token用4/8位低精度存储，最高可降低75%的KV cache内存占用

  - 搜索/推荐的query理解、文案生成等在线推理场景可借鉴动态资源调度逻辑：基于token embedding L1范数+query相似度打分，对低价值token降秩降精度计算，可提升2倍以上推理吞吐

  - 端侧小模型部署可复用离线维度排序方法：离线用SVD/PCA按激活方差重排隐层维度，运行时直接截断低方差维度，无额外 runtime 开销即可实现30%以上的推理加速'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Transformer/LLM端侧部署受限于静态推理的高能耗、高内存开销，传统静态量化、LoRA等方法对所有token统一分配计算资源，忽略了80%左右的低语义价值token（停用词、标点、冗余填充）的存在，浪费大量边缘设备算力与电量，难以支撑移动端电商导购、端侧推荐等场景的长序列推理需求。
### 方法关键点
- 离线校准：对预训练模型每层激活做SVD/PCA，按方差降序重排隐层维度，保证前r个维度包含最高价值信息，无任何运行时开销
- 在线显著性引擎：通过前向Hook实时计算每个token激活的L1范数，结合与用户query的余弦相似度得到综合显著性分，将token分为高/中/低三档，分别对应16位/128秩、8位/43秩、4位/8秩的计算配置
- 软硬件协同：45nm工艺下实现带细粒度时钟门控的脉动阵列，根据token等级动态关断未使用的计算单元、采用窄位宽写回SRAM，额外硬件开销仅1.62%
### 关键结果
在代码生成、逻辑推理、长摘要三类任务上测试，对比静态全精度基线、动态低秩RankDyna、动态剪枝DynamicViT等SOTA，45nm CMOS硬件下实现**59.2%的系统能耗降低**，**2.24倍吞吐提升**，仅带来3.6%的精度损失，EDAP（能耗-延迟-面积乘积）比最优基线低35%以上。
### 核心结论
Transformer推理中80%的语义价值集中在20%的token上，针对token的动态资源分配能在几乎不影响业务效果的前提下带来数倍能效提升。
