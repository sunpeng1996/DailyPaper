---
title: Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval
title_zh: 哪个小矮人？Doppeldwarf-306数据集与高度相似实例检索
authors:
- Turhan Can Kargin
arxiv_id: '2611.27490'
url: https://arxiv.org/abs/2611.27490
pdf_url: https://arxiv.org/pdf/2611.27490
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 相似实例检索 · 数据集与预训练模型验证
tags:
- Instance Retrieval
- DINOv2
- Dataset
- Similarity Matching
- Computer Vision
one_liner: 公开Doppeldwarf-306高相似雕像数据集，验证多预训练模型在相似实例检索的性能
practical_value: '- 电商同款/高相似SKU召回可直接采用DINOv2冻结特征+KNN的零训练基线，落地成本低效果优异

  - 带地理属性的到店商品/POI检索不要用位置直接过滤候选集，改为位置加权打分可大幅提升准确率

  - 高相似实例拒识场景无需额外训练，仅比对Top2候选置信度差值即可将误接受率降低近50%'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有实例检索基准多聚焦地标等高区分度物体，缺乏同系列高相似小物体的测试场景，无法准确验证预训练模型在细粒度相似实例检索任务上的真实性能。
### 方法关键点
1. 开源Doppeldwarf-306数据集，包含306个同主题系列青铜矮人雕像的1691张授权图片，标注摄影师信息；
2. 对比7种预训练范式下13个backbone的零训练检索性能，验证地理信息使用方式、局部特征匹配、Top候选比对对效果的影响。
### 关键结果
冻结DINOv2特征+KNN留一法检索准确率达93.1%，最优backbone准确率达94.7%；位置信息从过滤改为加权后，25米范围内用户检索准确率从93.4%升至98.7%；Top2候选比对可将未知实例误接受率从38.3%降至19.6%
