---
title: Scaling Articulated Rationales for MLLM-based Recommendation
title_zh: 面向多模态大模型推荐的显式用户理由规模化应用框架
authors:
- Haoke Xiao
- Yueyang Liu
- Yuhui Zhang
- Xiang Chen
- Yufei Liu
- Jia Xu
- Yalong Guan
- Xiaolan Zhu
- Xiaoyu Zhang
- Shijun Wang
affiliations:
- Kuaishou Technology
arxiv_id: '2609.17639'
url: https://arxiv.org/abs/2609.17639
pdf_url: https://arxiv.org/pdf/2609.17639
published: '2026-09-15'
collected: '2026-09-17'
category: GenRec
direction: 生成式推荐 · 显式用户偏好理由规模化
tags:
- MLLM4Rec
- Articulated Rationale
- Semantic ID
- DPO
- Ranking Optimization
one_liner: 首个工业级显式用户偏好理由规模化框架SARA，落地快手直播推荐实现效果提升
practical_value: '- 可复用显式用户反馈采集工程方案：采用10s延迟触发+5%基线动态概率投放+优质反馈返激励的问卷机制，平衡数据采集规模与用户体验，解决显式偏好信号稀疏问题

  - 可复用领域MLLM对齐流程：低资源场景下采用SFT+Quality-Refining DPO两阶段微调方案，通过自采样+多维度Agent Judge构造偏好对，大幅提升生成内容的业务适配性

  - 可复用生成特征落地排序的范式：无需改动排序模型主结构，可选择两种集成方式：一是生成文本Embedding进跨注意力交互模块，加MIM损失对齐语义；二是把生成文本量化为Semantic
  ID进负反馈历史建模，实现跨内容信号迁移

  - 可复用LLM评估器框架：采用单通轻量在线LLM Judge+多维度Agent离线Judge的双层评估架构，适配实时激励、离线数据清洗、偏好对构造等多场景需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统依赖点击、观看时长、负反馈等隐式行为信号，仅能反应用户行为结果，无法解释偏好背后的核心原因，细粒度可迁移的用户偏好建模能力受限。显式用户理由（AUR）作为带极性的原因级文本信号价值极高，但存在天然稀疏、表达质量低、通用MLLM生成内容无真实依据等问题，难以直接落地工业推荐系统。
### 方法关键点
- 数据引擎：面向2.4亿快手直播用户，采用10s延迟触发+动态概率投放+质量达标返激励的问卷机制采集AUR，经6维度Agent Judge筛选得到18.7万条高质量作者中心极性理由数据集SARA-HQ
- 理由生成对齐：基于Qwen2.5-VL-7B做两阶段微调，第一阶段用SARA-HQ做SFT学习极性理由生成，第二阶段用自采样+Agent Judge排序构造偏好对做QR-DPO优化，得到SARA-7B，将理由覆盖从8.6万创作者扩展到1000万
- 理由特征集成：两种落地范式，一是理由Embedding进排序模型跨注意力交互层，加MIM损失对齐用户-作者交互与理由语义；二是将负向理由量化为三级Semantic ID，进用户负反馈历史建模实现跨作者负信号迁移，得到SARA-Ranker
### 关键结果
离线评估显示SARA-7B比通用MLLM基线的理由质量得分提升27%，Agent Judge与人工标注的MAE低至0.2，接近人工一致性上限0.12；线上A/B测试显示SARA-Ranker使直播 engagement 提升4.2%，负反馈降低3.8%，已全量部署超30天。
### 核心结论
显式用户理由可作为工业推荐系统的一等信号，通过采集-生成-集成的标准pipeline即可落地获得明确业务收益。
