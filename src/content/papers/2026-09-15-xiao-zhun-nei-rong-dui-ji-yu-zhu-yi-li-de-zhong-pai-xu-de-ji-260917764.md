---
title: How Calibration Content Shapes Attention-Based Reranking
title_zh: 校准内容对基于注意力的重排序的影响机制与优化方法
authors:
- Petros Karypis
- Hossein Rajaby Faghihi
- Peter Chen
- Rui Zhu
- Noveen Sachdeva
- Yan Zhu
- Julian McAuley
affiliations:
- UC San Diego
- Google
- Google DeepMind
arxiv_id: '2609.17764'
url: https://arxiv.org/abs/2609.17764
pdf_url: https://arxiv.org/pdf/2609.17764
published: '2026-09-15'
collected: '2026-09-17'
category: RecSys
direction: 搜索重排序 · 注意力校准优化
tags:
- Reranking
- InContextRanking
- AttentionCalibration
- LLM
- Search
one_liner: 提出无训练的插值空查询校准方法，解决带复杂指令的注意力重排序性能退化问题
practical_value: '- Prompt工程优化：基于注意力的重排序场景下，若需模型遵循复杂指令（如电商个性化需求、用户persona、排除类约束），需将指令放在Query侧而非文档前的前缀位置，才能进入Query→Document注意力读出行列，确保指令生效。

  - 校准策略适配：根据指令类型选择校准方案，全场景复用的通用规则（如「排除预售款」）用标准λ=1校准；单Query专属的个性化指令（如用户定制化检索需求）用λ=0的裸空校准，可直接避免有效信号被误删。

  - 无训练性能提升：部署注意力重排序时可直接复用插值校准方案，仅新增1次前向推理开销，即可在带复杂指令的任务上获得最高3倍nDCG提升，效果超过生成式重排序RankGPT。

  - ICL低成本增益：直接加入1个BM25检索的同任务演示示例，即可为BEIR类通用检索任务带来0.04-0.07的nDCG提升，且不受校准策略干扰，无需额外调优。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于注意力的上下文重排序（ICR）仅需Prefill无需解码，推理效率比RankGPT等生成式重排序高1个数量级，是工业界大模型重排序的主流候选方案。当前主流ICR依赖空查询（N/A）校准消除位置偏置，但该方案假设空查询仅捕捉位置等无关信号，当Prompt加入复杂指令、用户Persona、约束条件时，空查询校准会误删和指令相关的有效相关性信号，导致重排序性能暴跌，现有工作均将校准步骤作为固定模块未做优化。

### 方法关键点
- 设计三Pass分解框架，将前向过程拆分为【查询+指令】、【空查询+指令】、【空查询无指令】三类，量化指令在空查询Pass中的信号足迹，区分足迹为惰性、无关偏置、有效信号三类；
- 设计无训练的插值空查询校准，引入超参数λ∈[0,1]，对两类空查询的得分做线性插值作为校准基线，λ=1恢复标准校准，λ=0完全剔除指令对校准的影响；
- 明确指令放置规则：仅当指令放在Query侧（属于Query→Document注意力的读入区域），才能有效引导重排序遵循指令约束。

### 关键实验
在BEIR、ExcluIR、NevIR、InstructIR、FollowIR等基准上测试，对比标准ICR、QRHeads、RankGPT基线：1）在带长个性化Persona的InstructIR任务上，标准校准nDCG仅0.275，插值校准（λ=0）nDCG达0.825，超过RankGPT的0.587，搭配QRHeads后进一步提升至0.894；2）加入1个上下文演示即可为BEIR任务带来0.04-0.07的nDCG提升，不受校准影响；3）该规律在4B-14B的Gemma-3、Qwen3、Llama-3.1模型上均稳定成立。

最值得记住的一句话：不要把注意力重排序的校准步骤作为无需调优的固定模块，其效果完全取决于空查询Pass中的指令信号是无关偏置还是有效相关性信号。
