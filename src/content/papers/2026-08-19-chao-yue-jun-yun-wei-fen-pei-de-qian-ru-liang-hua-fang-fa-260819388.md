---
title: Quantization Beyond Uniform Bit Allocation
title_zh: 超越均匀位分配的嵌入量化方法
authors:
- K. S. Sreeramji
- Sabyasachi Basu
- Ravishankar Krishnaswamy
- Kirankumar Shiragur
- Yujia Wang
affiliations:
- Indian Institute of Science
- Microsoft Research
- Microsoft STCA
arxiv_id: '2608.19388'
url: https://arxiv.org/abs/2608.19388
pdf_url: https://arxiv.org/pdf/2608.19388
published: '2026-08-19'
collected: '2026-08-21'
category: RecSys
direction: 推荐召回·MRL嵌入非均匀量化
tags:
- Quantization
- Matryoshka Representation Learning
- Product Quantization
- Scalar Quantization
- Embedding Retrieval
one_liner: 针对具备Matryoshka特性的嵌入提出贪心非均匀位分配方案，同等内存下提升PQ/SQ量化召回
practical_value: '- 对于已使用MRL特性嵌入（如OpenAI/Cohere商用嵌入）的电商搜索/推荐召回场景，可直接基于维度方差先验给前置维度分配更多量化位，低比特场景下无需额外训练即可提升召回率

  - 落地时可复用论文的贪心位分配框架，先将嵌入按连续维度分桶，用小流量验证集迭代选择最优位分配策略，适配自身业务的嵌入分布

  - SQ量化场景下可参考论文的位宽分配规则，避免1bit量化，用{0,2,4,8}bit档位结合均匀步长升级维度，平衡量化质量与工程实现复杂度

  - 低内存预算场景（如端侧推荐、超大规模向量库）优先尝试非均匀量化，相比均匀分配SQ最高可提18%召回，投入产出比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前大模型生成的嵌入维度普遍达到上千维，超大规模向量检索的存储、算力成本陡增。现有PQ、SQ等主流量化方案均为跨维度均匀分配比特，未利用当前商用嵌入普遍具备的Matryoshka（MRL）特性——前置维度集中了绝大部分语义信息，均匀分配在低比特场景下效率极低，亟需适配嵌入结构的量化方案，在控制成本的同时保证召回质量。

### 方法关键点
- 核心框架：将嵌入的连续维度划分为等长桶，基于贪心策略迭代分配比特增量，每次把额外比特分配给能带来最大召回提升的桶，直到达到总内存预算
- PQ适配：每个桶内按分配的比特数动态划分亚向量，训练独立的256中心k-means码本，余出维度优先分配给前置亚向量
- SQ适配：采用{0,2,4,8}bit的位宽档位，避免1bit量化带来的分布失真，桶内先设基础位宽，剩余比特按均匀步长升级部分维度的位宽，无额外元数据开销

### 关键实验结果
在MS Marco、Quora等6个公开检索数据集上，对比均匀位分配的PQ、SQ基线，使用OpenAI text-embedding-3-large、Cohere embed-v4两个主流MRL嵌入验证：同等压缩率下，非均匀分配相比基线PQ召回最高提升8%，SQ召回最高提升18%，低比特（<1bpd）场景下增益最为显著。

### 核心结论
针对MRL特性嵌入，仅靠调整位分配策略无需修改量化逻辑或重新训练模型，即可在同等存储预算下获得显著的召回提升。
