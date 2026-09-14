---
title: 'UniPart: Towards Zero-shot Language-Grounded 3D Part Segmentation for Embodied
  Interaction'
title_zh: UniPart：面向具身交互的零样本语言对齐3D部件分割
authors:
- Xinqiang Yu
- Zekun qi
- Jiawei He
- Wenyao Zhang
- Xuchuan Chen
- Guaocai Yao
- Li Yi
- Zhaoxiang Zhang
- He Wang
affiliations:
- Chinese Academy of Sciences
- Peking University
- Tsinghua University
- Shanghai Jiao Tong University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2609.12898'
url: https://arxiv.org/abs/2609.12898
pdf_url: https://arxiv.org/pdf/2609.12898
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: 具身Agent · 3D语言对齐语义理解
tags:
- Zero-Shot Learning
- 3D Part Segmentation
- Cross-Modal Transformer
- Embodied Agent
- CLIP
one_liner: 提出基于CLIP文本嵌入的跨模态3D Transformer UniPart，实现零样本开放词汇3D部件分割支撑具身交互
practical_value: '- 布局具身电商（仓储拣选、虚拟3D商品交互）的团队可复用UniPart跨模态对齐逻辑，用自由文本指令定位3D商品功能部件，响应用户操作需求

  - 跨模态数据集构建可借鉴LangPart的多视图一致性弱标注思路：先大规模生成文本-部件配对，再小批量人工标注做微调，大幅降低标注成本

  - 零样本跨模态检索/分割任务可复用「预训练大模型文本嵌入作为条件输入单模态Transformer」的架构，无需端到端重训大模型，落地成本低'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有3D基础模型存在明显能力gap：要么泛化性强但仅支持整物识别，要么可识别部件但局限于闭集分类，无法支撑开放场景下具身Agent的细粒度操作需求，零样本迁移能力弱。
### 方法关键点
1. 提出UniPart前馈跨模态3D Transformer，直接以CLIP文本嵌入为条件输入，实现自由文本引导的点云部件分割；
2. 构建LangPart-1M大规模弱标注数据集，覆盖16万+ Objaverse资产，生成800万文本-部件配对，基于多视图一致性保证标注质量；
3. 人工标注LangPart-4K高质量子集用于模型微调与效果评测。
### 关键结果
在开放词汇3D部件分割基准上取得SOTA零样本效果，可直接迁移到真实场景下的语言引导部件抓取任务。
