---
title: Constraint-Aware Conversational Job Recommendation in Code-Mixed Low-Resource
  Settings
title_zh: 面向低资源语码混合场景的约束感知会话式职位推荐
authors:
- Md Arman Hossain
- Mubashir Jawad
- Fariha Khandaker Moon
- Sonia Binte Siraj
- Masfiqur Rahaman
- Raihan ul Islam
- Ahmed Wasif Reza
- Nafis Sadeq
affiliations:
- East West University
- University of California San Diego
arxiv_id: '2610.05787'
url: https://arxiv.org/abs/2610.05787
pdf_url: https://arxiv.org/pdf/2610.05787
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 会话式推荐 · 多准则软约束排序
tags:
- Conversational Recommendation
- Soft Constraint
- Code-Mixed
- Low Resource
- Multi-Criteria Ranking
one_liner: 提出软约束多准则排序框架W-SCAR及多语言会话职位基准，解决硬过滤不可逆召回损失问题
practical_value: '- 约束类推荐场景（如电商高筛选条件品类、招聘、租房）可放弃前置硬过滤，改用软约束加权排序，避免属性抽取/归一化误差导致的召回损失，尤其适合低资源业务

  - 多语言/混合语言搜索推荐场景，可融合BM25稀疏检索与多语种密集检索的互补信号：纯英文用密集检索效果更优，罗马化混合语言BM25 lexical匹配效果更好

  - 多维度排序冷启动场景可复用AHP+TOPSIS多准则加权框架，无需标注训练，仅靠业务先验确定权重即可上线，落地成本低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
会话式推荐需要同时兼顾语义相关性、用户动态偏好、品类/任职资格等约束条件，在低资源语码混合场景下，传统前置硬约束过滤会因为对话偏好提取误差、属性归一化不一致，不可逆地筛掉原本匹配的候选，现有方案大多针对高资源单语言场景设计，对噪声输入鲁棒性差。
### 方法关键点
- 构建JobCCC基准数据集：包含22410条结构化职位数据、988条标注多轮职业咨询对话，同步提供语义等价的英文、罗马化孟英混合（Banglish）双版本语料，所有对话标注动态偏好与关联的真值职位
- 提出W-SCAR排序框架：融合6维信号，包括BM25 lexical relevance、多语种E5 dense相似度、经验/地域/学历/薪资4个维度的软约束效用分（不匹配给梯度惩罚而非直接过滤，属性未命中时给中性分）
- 无需额外训练，通过AHP确定6维特征权重，再用TOPSIS计算每个候选与理想解的接近度作为最终排序分
### 关键实验
在JobCCC数据集上对比BM25、硬过滤+BM25、多语种密集检索、硬过滤+密集检索4类基线：硬过滤会使所有基线Hit@10下降30%~45%；W-SCAR在Banglish场景Hit@10达38.43%，比硬过滤+密集检索高18.96个百分点；在英文场景Hit@10达37.37%，跨语言性能差仅1.06%，远低于单一路由的检索方案。
### 核心结论
带约束的会话式推荐在噪声多、属性不规范的场景下，更适合建模为软约束多准则排序问题，而非先做硬过滤再做相关性检索
