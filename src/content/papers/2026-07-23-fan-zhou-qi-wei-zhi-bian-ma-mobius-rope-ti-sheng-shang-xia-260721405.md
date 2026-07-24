---
title: 'Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context
  Retrieval Reliable'
title_zh: 反周期位置编码Möbius RoPE：提升上下文检索可靠性
authors:
- Ji Ho Bae
affiliations:
- JRTI, Seoul, Republic of Korea
arxiv_id: '2607.21405'
url: https://arxiv.org/abs/2607.21405
pdf_url: https://arxiv.org/pdf/2607.21405
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 大语言模型 · 位置编码优化
tags:
- Positional Encoding
- RoPE
- In-Context Retrieval
- Pretraining Stability
- Anti-periodic Boundary
one_liner: 提出基于反周期边界的Möbius RoPE 零成本消除小模型上下文检索的种子随机性
practical_value: '- 训练面向RAG/Agent的小尺寸垂直领域LLM时，可直接复用混合Möbius RoPE方案：仅修改25%注意力头的频率表，无参无额外FLOPs，几乎不影响perplexity，同时大幅降低检索能力的种子随机性，避免训练出损失正常但检索拉胯的模型

  - 小模型（≤160M参数）优先用单尺度Möbius RoPE，中等模型（≥410M参数）优先用多尺度阶梯式Möbius头分配，可同时保障训练窗口内检索可靠性和外插性能

  - 做RAG检索效果评估时，需要警惕种子随机性带来的模型性能偏差，不能仅用perplexity判断模型的检索能力，必须加入NIAH类的基准测试

  - 业务上如果只需要短上下文（≤训练窗口）的可靠单事实检索，可以考虑NoPE方案，但要接受13%的perplexity损失和长上下文性能下降的trade-off'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
小参数LLM训练时，上下文检索能力存在严重的种子彩票问题：相同配置不同随机种子训练的模型，NIAH（大海捞针）准确率波动极大，最低14%最高98%，且这种波动完全无法通过perplexity等常规训练指标预警，给RAG、Agent类依赖上下文检索的业务场景带来极大的不可控风险。

### 方法关键点
- 提出Möbius RoPE：采用反周期频率阶梯$\theta_i=\pi(2i+1)/N$，位置全环绕的holonomy为-1，形成序列两端确定性耦合的Dirichlet偶极子结构，长距离位置信号不会乱序
- 混合方案：仅给25%的注意力头配置Möbius RoPE，剩余75%沿用标准RoPE，无新增参数、无额外FLOPs，仅修改部分头的正余弦常量表
- 设置同频带非周期、周期（holonomy+1）RoPE、NoPE等对照组，隔离反周期边界的核心作用

### 关键结果
在160M、410M两个尺度的模型上，各用2B FineWeb-Edu tokens预训练，对比标准RoPE baseline：
- 160M模型：perplexity基本持平（29.66 vs 29.72），L=512时NIAH准确率的跨种子方差降低30.8倍，最差种子准确率从14%提升到86%，稳健方差检验p=0.013-0.029
- 410M模型：方差降低效果依然显著（SD 6.5% vs 16.5%，L=2048，Levene p=0.040），多尺度阶梯分配的Möbius RoPE外插性能最优
- 消融实验证明：仅反周期边界能带来可靠性提升，同频带非周期、周期RoPE分别仅能实现1倍、3.1倍的方差降低，冻结权重换回标准RoPE会直接让检索准确率暴跌到41.7%

最值得记住的一句话：仅修改25%注意力头的RoPE频率表，就能零成本为训练窗口内的单事实检索能力提供「抗种子随机保险」，且不损失语言建模性能
