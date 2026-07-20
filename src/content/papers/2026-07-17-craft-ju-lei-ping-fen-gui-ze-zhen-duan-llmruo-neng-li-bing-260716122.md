---
title: 'CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted
  Fine-Tuning Data'
title_zh: CRAFT：聚类评分规则诊断LLM弱能力并生成定向微调数据
authors:
- Vipul Gupta
- Zihao Wang
- Razvan-Gabriel Dumitru
- MohammadHossein Rezaei
- Aakash Sabharwal
- Yunzhong He
affiliations:
- Scale AI
arxiv_id: '2607.16122'
url: https://arxiv.org/abs/2607.16122
pdf_url: https://arxiv.org/pdf/2607.16122
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: LLM微调 · 弱能力诊断与定向数据生成
tags:
- LLM Fine-tuning
- Rubric Clustering
- Capability Diagnosis
- Targeted Data Generation
- Hierarchical Evaluation
one_liner: 基于rubric聚类构建分层能力树，动态识别LLM弱能力定向生成微调数据提升领域性能
practical_value: '- 做垂直领域Agent（如电商智能客服、商品合规审核、广告文案生成Agent）时，可将业务输出要求拆解为独立rubric评分点，复用CRAFT思路精准定位模型缺失能力，相比随机添加域内数据，微调效率提升更显著

  - 自定义微调数据集时，可借鉴动态跨层级选弱节点的策略，无需固定能力分析粒度，根据能力树各层级通过率灵活选择补全的能力点，相同数据预算下业务效果提升更明显

  - 构建业务LLM评估体系时，可将rubric作为能力探针，聚类生成场景专属能力树，既能快速定位badcase根因，也能直接对接微调数据生成流程，实现评估-迭代的全闭环'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM评估仅能定位模型在哪些任务/类别上表现差，无法明确具体缺失的能力点，难以直接指导后续微调数据收集；单任务低分往往混杂多种独立能力故障，泛泛补充同领域数据效率极低，无法针对性补全模型短板。
### 方法关键点
- 将每个prompt-rubric（评分规则）对拆解为独立能力探针，提取对应的能力描述，替代传统prompt级别的粗粒度分析
- 自底向上构建分层能力树，支持对接已有业务分类标签作为顶层节点，树深度根据数据规模自适应生成，无需预定义固定超参数
- 统计目标模型在能力树每个节点的通过率，采用动态跨层级搜索选择弱能力节点，选中节点的上下子孙/祖先节点自动排除，避免重叠，保证每个弱能力的粒度最优
- 基于选中的弱能力节点生成定向微调数据，生成时引入父/兄弟节点上下文，避免能力重叠
### 关键实验
在金融、法律两个专业领域测试4个开源模型（Qwen3-4B/8B、Gemma-3-4B、Llama-3.1-8B-Instruct），对比EvalTree（prompt层级聚类）、随机生成数据两个基线：金融领域CRAFT在4个模型上均取得最优平均得分，最高超基线5.9分；法律领域3个模型最优，1个模型与最优基线得分在方差范围内；动态选节点比固定层级选点平均提升1-3个百分点。
### 核心结论
评估的核心价值不止是输出得分，更要解释模型为什么失败，并将诊断结果直接转化为可执行的迭代方案，才能最大化评估的业务价值。
