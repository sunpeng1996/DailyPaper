---
title: 'AGR: Agentic Generative Retrieval with Tool-Augmented Search'
title_zh: AGR：工具增强的智能体生成式检索框架
authors:
- Ming Yang
- Yaqi Yin
- Zhibo Wang
- Xiaoze Jiang
- Jingwei Zhuo
- Chao Zhang
- Quanzhi Zhu
- Weiguo Zheng
- Liang Zeng
- Yunfeng Zhao
affiliations:
- Fudan University
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2610.26831'
url: https://arxiv.org/abs/2610.26831
pdf_url: https://arxiv.org/pdf/2610.26831
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式检索 · 工具增强智能体
tags:
- Generative Retrieval
- Semantic ID
- Tool Augmented
- Agent
- Feature Injection
one_liner: 将工具调用与Semantic ID生成融合，实现生成式检索的按需自适应异构特征注入
practical_value: '- 异构特征封装为可调用工具，无需全量注入输入，根据SID解码前缀动态调用，既能降低推理成本，又可避免无关特征引入的噪声，适配工业界多特征场景的落地需求

  - 工具调用训练数据可基于特征适用性（与正样本匹配）和信息增益（SID层级区分度最高位置）规则构造，配合两阶段训练+自适应损失缩放，无需RL即可快速落地，训练稳定性更高

  - 长序列用户行为无需全量拼接入输入，可通过投票/注意力方式压缩为单个observation token注入，工业场景下和直接拼接400个行为序列效果相当，训练时间降81.8%、推理成本降42.9%

  - 工具调用无需全量触发，仅在基线难例上调用即可获得收益，AGR线上平均延迟仅35ms，符合搜索/推荐场景的低延迟要求，可直接复用至电商搜索、商品推荐等场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索（GR）静态特征注入方案存在两个核心瓶颈：一是特征效用高度依赖请求，全量注入会引入大量噪声，同时大幅抬升训练和推理成本；二是hierarchical Semantic ID 不同层级对应不同粒度的语义，固定位置注入特征无法匹配各层级的信息需求，特征无法发挥最大效用，难以平衡工业场景的效果与成本。
### 方法关键点
- 架构设计：将结构化/序列类异构特征封装为工具，扩展词表加入工具token与观测token，把Semantic ID生成和工具调用统一到自回归解码流程，根据当前请求与已解码SID前缀，动态决策是否调用工具、调用哪类工具，返回的观测token注入后续解码，引导生成特征一致的SID分支。
- 训练数据构造：基于两个规则构造工具增强样本：①when：仅当特征与正样本匹配、且未出现在已有输入上下文时插入工具调用；②where：选择SID层级中特征区分度提升最大的位置插入，确保特征在最有效的层级生效。
- 训练流程：采用两阶段训练，第一阶段预训练纯SID生成能力，第二阶段微调工具调用能力，通过自适应损失缩放平衡SID token与工具token的损失权重，避免破坏预训练语义表示。
### 关键实验
在快手工业搜索数据集、Qilin、JDSearch、KuaiSAR 4个数据集验证，对比TIGER、UniSearch、GEMs等SOTA GR基线，工业数据集Recall@32最高提升14.04%，MRR@32提升19.53%；线上A/B测试搜索相关性提升0.205%，query改写率下降0.69%，平均延迟35ms符合线上要求。
### 核心结论
生成式检索的特征注入不需要静态全量注入，按需动态调用特征可以在更低成本下取得更优效果。
