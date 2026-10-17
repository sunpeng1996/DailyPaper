---
title: Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization
title_zh: MoE大模型个性化场景下的专家角色可解释性研究
authors:
- Sekh Mainul Islam
- Pepa Atanasova
- Isabelle Augenstein
affiliations:
- University of Copenhagen
arxiv_id: '2610.22127'
url: https://arxiv.org/abs/2610.22127
pdf_url: https://arxiv.org/pdf/2610.22127
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: LLM 个性化 · MoE 可解释性
tags:
- MoE
- Personalization
- Interpretability
- Crosscoder
- PEFT
one_liner: 提出两阶段微调MoE加Crosscoder框架，实现个性化特征的专家级定位与可解释性
practical_value: '- 电商/推荐场景做LLM个性化适配优先选用MoE架构：仅激活20%总参数即可达到同总参稠密LLM的个性化效果，推理成本降低近80%，适配高吞吐需求

  - MoE个性化微调可复用两阶段PEFT方案：先仅调路由器筛选个性化相关专家，再仅微调Top高频专家，训练成本远低于全量/全MoE微调

  - 可通过Crosscoder定位不同用户群偏好对应的专属专家，定向boost对应专家即可实现偏好切换，无需全模型调整，适配多人群个性化文案生成、导购话术等场景

  - MoE的低多义性专家特征可解决黑盒LLM个性化难归因的问题，符合推荐/广告场景的合规性要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有稠密LLM的个性化方案受神经元多义性限制，无法定位不同个性化特征对应的模型组件，难以解释、干预个性化输出，无法满足推荐/广告等场景对可控、可解释个性化的需求。MoE LLM的稀疏路由机制天然降低了特征多义性，专家级的模块化结构为个性化特征的定位提供了可能。
### 方法关键点
1. 两阶段PEFT微调MoE：先冻结专家与其他参数仅微调路由器，统计训练集中各专家被选中的频率；再仅微调每层激活频率Top k的个性化相关专家，大幅降低训练成本
2. 训练Crosscoder对齐个性化与非个性化MoE的配对激活，学习高维稀疏隐空间，通过隐向量的相对范数差筛选仅属于个性化模型的专属隐特征
3. 统计各隐特征激活时的专家路由分布，建立个性化特征到对应专家的映射关系，验证映射的稳定性与特征区分度
### 关键实验
在Multifaceted Collection、LaMP、LongLaMP三个覆盖群体/个体级偏好的个性化数据集上测试，对比3款开源MoE（OLMoE-1B-7B、Qwen3-30B-A3B、Mixtral-8x7B）与同活跃参/同总参稠密LLM：
- MoE仅激活20%总参数，性能超过同活跃参稠密LLM，匹配同总参稠密LLM的个性化效果
- 仅需不到0.25%的隐向量即可覆盖全部个性化特征，不同特征对应专属专家的区分度达0.94，映射稳定性达0.81
- 定向boost对应个性化特征的专家，可让非个性化模型的输出与个性化模型的KL散度下降超80%
### 核心结论
MoE的稀疏路由特性不仅能降低个性化的训练推理成本，还能实现个性化特征的可定位、可干预，是可控可解释个性化LLM的优选架构
