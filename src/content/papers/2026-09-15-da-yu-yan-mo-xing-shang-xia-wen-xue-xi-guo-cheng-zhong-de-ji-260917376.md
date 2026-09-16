---
title: Large Language Models Develop Belief State Geometry In-Context
title_zh: 大语言模型上下文学习过程中的信念状态几何表征机制
authors:
- Daniel Balcells
- Andrew Jun Lee
- Chirag Rastogi
- Paul M. Riechers
- Adam Shai
- Xavier Poncini
affiliations:
- Independent
- UCLA
- UIUC
- Simplex
- Astera Institute
arxiv_id: '2609.17376'
url: https://arxiv.org/abs/2609.17376
pdf_url: https://arxiv.org/pdf/2609.17376
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM 上下文学习内在表征机制
tags:
- In-context Learning
- Belief State
- Hidden Markov Model
- Residual Stream
- Linear Probing
one_liner: 验证开源LLM上下文学习HMM序列时残差流可线性解码信念状态且与预测因果相关
practical_value: '- 开发LLM驱动的推荐/导购Agent时，可通过Linear Probe直接从残差流提取用户隐式信念状态（如偏好、决策阶段），无需额外微调即可实现细粒度状态跟踪

  - 长序列用户行为建模场景下，可借鉴信念子空间steering/patching方法，定向修正LLM对用户兴趣漂移的预测偏差，提升长周期推荐准确度

  - 做ICL prompt优化时，可参考信念状态收敛的token窗口阈值，合理控制上下文长度，减少冗余输入带来的计算损耗'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有ICL研究多聚焦行为层面，对支撑ICL的底层表征机制理解不足，缺乏可证伪的理论预测。选择HMM作为受控场景（其信念状态即隐状态后验分布有明确定义），可验证生产级LLM做ICL时是否遵循贝叶斯推断的表征逻辑。
### 方法关键点
- 覆盖6款主流开源LLM：Qwen3.5-9B/4B、Llama3.1-8B、Llama3.2-3B、Gemma-4-E4B/E2B
- 构造40个非平凡信念结构的HMM（30个为全新设计），生成20k长度的token序列作为prompt
- 用Linear Probe从各层残差流激活中解码信念状态，通过子空间patching/steering干预验证因果相关性
- 用tuned lens验证信念状态可解码性与早退出预测精度的关联
### 关键结果数字
- 信念状态线性探测R²峰值范围0.83~0.99，在不同LLM与HMM组合中覆盖早至晚各层
- 定向干预信念子空间后，模型预测KL与未篡改模型相当，随机干预对照组性能下降显著
- ICL预测在输入5k~10k token后收敛，等效于k=3.4~11.0阶的马尔可夫预测器
### 核心结论
开源LLM的上下文学习本质是对上下文推断出的生成模型做近似最优贝叶斯预测，信念状态线性编码在残差流中且对下游预测起因果作用
