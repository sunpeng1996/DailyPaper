---
title: 'YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family'
title_zh: YOLO-PEFT：面向YOLO系列模型的参数高效微调框架
authors:
- Xu Lin
- WenJie Nie
- Jinlong Peng
- Weifu Fu
- YueXiao Ma
- Xiawu Zheng
- Yong Liu
affiliations:
- Tencent
- Xiamen University
arxiv_id: '2608.07051'
url: https://arxiv.org/abs/2608.07051
pdf_url: https://arxiv.org/pdf/2608.07051
published: '2026-08-06'
collected: '2026-08-10'
category: Training
direction: 视觉检测器 · 参数高效微调框架优化
tags:
- PEFT
- LoRA
- YOLO
- Object Detection
- Fine-Tuning
one_liner: 优化异构检测器adapter放置策略，YOLO系列PEFT效果超全量微调且省显存
practical_value: '- 电商商品识别/搜图业务的YOLO系列模型微调可直接复用该框架，相比全量SFT节省40%+训练显存，效果更优

  - 适配新类目/新拍摄场景的检测器迭代时，可参考其adapter放置的约束规划逻辑，减少手动试错成本

  - 多模态推荐的图像特征抽取模块微调时，可复用其PEFT有效性校验逻辑，提前规避灾难性退化问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
从NLP迁移的通用PEFT方法在实时检测器上易静默失效，检测器异构算子、专属组件的放置约束是常规Transformer结构不具备的，手动试错adapter放置方案成本极高。
### 方法关键点
将adapter放置建模为可审计的约束规划问题，结构感知的YOLO-PEFT框架输入检测器图、PEFT需求、资源预算后，自动校验算子有效性、检测器语义、图接口、部署四类约束，为每个排除模块记录原因，要么输出符合预算的目标模块规划，要么训练前直接返回Refuse规避无效训练。
### 关键结果
- VOC数据集上，框架选择的RS-LoRA在YOLO11s/YOLO12s上mAP50-95分别达0.7138/0.7307，较全量SFT的0.6428/0.6662大幅提升
- YOLO11训练中LoRA降低峰值显存43.9%，训练时长仅增加72%
- 针对RT-DETR-L可准确识别所有7种LoRA配置均超过灾难性退化阈值，提前输出Refuse决策
