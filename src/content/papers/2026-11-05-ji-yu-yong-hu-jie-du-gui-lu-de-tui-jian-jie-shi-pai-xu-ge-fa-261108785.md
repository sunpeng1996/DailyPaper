---
title: 'Learning from How Users Interpret: Personalizing Recommendation Explanation
  Order'
title_zh: 基于用户解读规律的推荐解释排序个性化方法
authors:
- Deo Munduku
- Elsa Negre
affiliations:
- Paris-Dauphine University, PSL Research University
- UMR CNRS 7243, LAMSADE
arxiv_id: '2611.08785'
url: https://arxiv.org/abs/2611.08785
pdf_url: https://arxiv.org/pdf/2611.08785
published: '2026-11-05'
collected: '2026-11-09'
category: RecSys
direction: 个性化推荐 · 推荐解释排序优化
tags:
- personalized-explanation
- recommendation-system
- user-profiling
- sentence-ordering
- user-comprehension
one_liner: 从用户历史文本解释提取三维特征构建画像，用于个性化排序推荐理由，显著提升用户对推荐解释的理解度
practical_value: '- 电商商品/服务推荐的解释文案可新增排序优化维度，在不修改内容的前提下提升用户理解度，降低用户决策成本

  - 可复用用户历史评论、咨询等公开文本的三维特征（信息选择、相对显著性、关联组织）构建用户画像，无需额外调研用户偏好

  - 推荐解释排序的轻量规则策略效果优于仅喂给LLM用户画像+上下文的方案，工程落地时可优先考虑规则排序降低算力成本

  - 做推荐解释效果评估时需区分用户客观理解度、主观满意度、推荐接受率三个指标，三者无必然正相关，避免单一指标误判'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有个性化推荐解释仅围绕内容、展示形式做适配，未捕捉用户解读信息时的组织习惯差异——相同偏好的用户对信息排序的接受度可能存在显著差异，且过往方法未利用用户历史文本解释中隐含的信息处理规律，无法在不改动解释内容的前提下提升信息传递效率，同时过往评估常混淆用户理解度和推荐接受率，无法准确衡量解释的实际效果。
### 方法关键点
- 从用户历史文本解释中提取三维特征构建静态用户画像：信息选择（用户关注的信息维度）、相对显著性（各维度的重视程度）、关联组织（不同维度信息的共同提及概率）
- 排序规则：先按特征显著性对解释句子降序排序，再将历史共现概率最高的两个维度的句子调整为相邻，其余句子相对顺序不变，全程不修改解释内容
### 关键结果
实验招募122名参与者，覆盖4类生活服务推荐场景，控制解释内容完全一致仅调整顺序，核心指标为用户客观理解正确率：
- 基于用户自身画像的排序方案（OWN）准确率达86.5%，较使用其他用户画像的DONOR（66.0%）高20.5pct，较群体画像的POP（63.9%）高22.6pct，较输入用户画像+上下文的Mistral-7B排序方案（PROFILE-LLM）高13.5pct，所有对比p值均<0.001
- 四种方案的推荐接受率无统计显著差异，说明理解度提升不直接带来转化提升
### 核心结论
个性化推荐解释的信息排序优化可在不改动内容的前提下大幅提升用户理解度，用户历史文本隐含的信息处理规律的价值远高于群体规律和通用LLM的适配效果。
