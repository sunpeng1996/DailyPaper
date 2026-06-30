---
title: 'Orca: The World is in Your Mind'
title_zh: 《Orca：学习统一世界隐空间的通用世界基础模型》
authors:
- Yihao Wang
- Yuheng Ji
- Mingyu Cao
- Yanqing Shen
- Runze Xiao
- Huaihai Lyu
- Senwei Xie
- Euan Liu
- Klara Tian
- Tianfeng Long
affiliations:
- Beijing Academy of Artificial Intelligence
arxiv_id: '2606.30534'
url: https://arxiv.org/abs/2606.30534
pdf_url: https://arxiv.org/pdf/2606.30534
published: '2026-06-29'
collected: '2026-06-30'
category: Multimodal
direction: 多模态通用世界基础模型预训练
tags:
- World Foundation Model
- Multimodal Pre-training
- Next-State-Prediction
- Unified Latent Space
- Embodied AI
one_liner: 提出双范式预训练的Orca通用世界基础模型，基于下一状态预测学习统一多模态世界隐空间
practical_value: '- 可借鉴双范式预训练思路：用高密度无标注连续行为序列做无监督隐式学习，搭配稀疏标注的关键事件做有监督显式学习，适配用户行为序列建模

  - 冻结主干+轻量模态解码器的下游适配方案可复用：大模型预训练后下游仅微调小参数头，大幅降低搜索/推荐/广告多场景落地成本

  - 统一隐空间建模思路可迁移至多模态推荐：打通用户行为、商品图文、搜索query的统一表征，提升跨域推荐效果'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型普遍孤立优化下一token、帧、动作预测目标，缺乏对世界状态转换的统一建模，难以适配跨模态、多类型下游任务的通用能力要求。
### 方法关键点
1. 以**Next-State-Prediction**为统一建模目标，替代离散的单模态预测任务，构建状态转换统一建模路径；
2. 双互补范式预训练：无意识学习从125K小时连续视频中捕捉稠密自然状态转换，有意识学习基于160M事件标注、VQA监督建模稀疏有意义的状态转换，学习统一世界隐空间；
3. 下游适配采用「冻结主干+仅微调轻量模态专属解码器」的低成本方案。
### 关键结果
在文本生成、图像预测、具身动作生成三类代表性下游任务上，性能超越同等参数量的专用基线模型，验证了世界隐空间质量越高、下游任务效果越好的scalability特性。
