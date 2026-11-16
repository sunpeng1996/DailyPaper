---
title: 'Deep Latents, Long Memory: Latent persistence explains temporal correlations
  in transformer activations'
title_zh: 深度隐变量长记忆：隐特征持久性解释Transformer激活的时序相关性
authors:
- Francesco Cagnetta
- Santiago Acevedo
affiliations:
- Simplex
- SISSA
arxiv_id: '2611.18089'
url: https://arxiv.org/abs/2611.18089
pdf_url: https://arxiv.org/pdf/2611.18089
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM可解释性 · 隐特征时序分析
tags:
- LLM
- Transformer
- SparseAutoencoder
- ActivationCorrelation
- FeaturePersistence
one_liner: 提出激活自相关度量，证明Transformer隐特征持久性随深度提升，解释激活时序相关性
practical_value: '- 做LLM4Rec长上下文用户行为建模时，优先用Transformer中间/深层特征捕捉长期用户兴趣，浅层特征更适合短期行为建模，因深层特征持久性更长

  - 可复用文中的激活自相关度量，验证垂域LLM（如电商导购Agent）是否有效编码长期会话特征，无需设计额外探针任务

  - 基于SAE提取的持久语义特征，可直接用于电商长会话的用户兴趣分段、话题识别，效果比纯文本聚类更贴合LLM内部语义表示'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
此前对LLM表征抽象性的量化缺乏统一可迁移的观测框架，无法直接关联合成数据的理论发现与真实预训练LLM的行为，需要无先验语义假设的探针方法刻画层间时序信息处理规律。

### 方法关键点
- 定义层激活自相关函数 $c_\ell(\tau)$ 为同层间隔 $\tau$ 个位置的激活向量归一化点积的均值，量化激活的时序相关性
- 用受控隐层次结构的合成数据Random Hierarchy Model（RHM）训练Transformer，验证自相关与隐特征持久性的对应关系
- 针对真实预训练LLM，用Sparse Autoencoder（SAE）提取的特征作为隐变量代理，定义特征持久性为连续激活的token长度，验证二者关联
- 通过消融持久SAE特征验证因果性，移除持久特征后观测自相关的下降幅度

### 关键结果
- 合成数据上，自相关随训练阶段逐步增长，每个台阶对应模型学会一级隐层次结构，隐特征编码可解释55~95%的自相关观测值
- 5个开源LLM（Gemma 2 2B/9B、Pythia-160M、Llama-3-8B、Qwen3-8B）在WikiText、The Pile数据集上，层集成自相关 $\chi_\ell$ 与SAE特征中位持久性的皮尔逊相关系数最高达0.93，二者均随深度单调增长
- 消融单个最持久SAE特征可使自相关下降3.2%~13.3%，消融全部活跃SAE特征可使自相关下降43.7%~68.3%，消融非持久特征无明显影响

### 核心结论
Transformer越深的层编码的语义隐特征在上下文里持续的时间越长，这种持久性是激活长程时序相关性的主要来源。
