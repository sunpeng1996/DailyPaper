---
title: More Reader Data or a Better Teacher? Updating a Model of Crowd Highlights
  in Late 2026
title_zh: 《更多用户阅读数据还是更强教师模型？2026年末人群高亮标注模型更新》
authors:
- Kazuki Nakayashiki
- Keisuke Watanabe
affiliations:
- Glasp Inc.
arxiv_id: '2610.17768'
url: https://arxiv.org/abs/2610.17768
pdf_url: https://arxiv.org/pdf/2610.17768
published: '2026-10-13'
collected: '2026-10-16'
category: RecSys
direction: 内容排序 · 用户行为与大模型优化效果对比
tags:
- Content Ranking
- LLM for Ranking
- User Behavior Data
- Knowledge Distillation
- Zero-shot Ranking
one_liner: 对比三类人群高亮排序模型优化方案，验证用户行为数据增益远大于大模型相关优化手段
practical_value: '- 细分场景排序任务优先扩增领域内用户行为数据，投入产出比远高于通用LLM零样本排序、大模型教师蒸馏的方案

  - 相同训练范式下，扩大模型参数量（3B→27B）的增益接近训练数据翻倍的增益，可根据算力成本二选一

  - 冷启动场景缺用户数据时，可采用LLM+轻量行为特征（如阅读位置）的融合方案做兜底排序，效果优于单通用LLM'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
社交高亮平台冷启动页面用户高亮标注不足，需模型预测人群关注的句子；新一代LLM发布后，三类优化路径的效果差异未明确：直接用LLM零样本排序、LLM作为教师蒸馏、扩增用户高亮训练数据。
### 方法关键点
固定评估规则与密封测试集，在215个开发页面、131个全新冷启动页面对比三类方案的句子排序平均精度。
### 关键结果
- 7款2026年10月前发布的LLM零样本排序AP最高0.3744，融合阅读位置特征后AP最高0.3931，远低于仅用用户高亮训练的3B模型的0.4346
- LLM作为教师解决用户标注冲突仅带来0.0013的非显著AP提升，训练数据从50%扩增到100%带来0.0242的显著提升
- 同训练范式下27B模型比3B模型AP高0.0225，增益接近数据翻倍效果，冷启动页面上二者表现无显著差异，均优于LLM融合方案
