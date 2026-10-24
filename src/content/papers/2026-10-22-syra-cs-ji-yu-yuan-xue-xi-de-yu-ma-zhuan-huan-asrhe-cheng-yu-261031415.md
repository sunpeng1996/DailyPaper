---
title: 'SyRA-CS: Synthetic-to-Real Adaptation for Code-Switched ASR with Meta-Learning'
title_zh: SyRA-CS：基于元学习的语码转换ASR合成到真实域适配方法
authors:
- Fadel Thior
- Ahmer Tabassum
- Haania Siddiqui
- Hanan Aldarmaki
- Thamar Solorio
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.31415'
url: https://arxiv.org/abs/2610.31415
pdf_url: https://arxiv.org/pdf/2610.31415
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 语码转换ASR · 元学习域适配
tags:
- Meta-Learning
- ASR
- Code-Switching
- Domain-Adaptation
- Synthetic-Data
one_liner: 基于Reptile元学习的语码转换ASR域适配框架，仅需1小时标注实采数据提效
practical_value: '- 多语言电商语音导购Agent的语码转换ASR优化可复用该范式：先基于低成本合成数据元训练初始化，再用少量实采标注数据微调，大幅降低标注成本

  - 元学习初始化比普通持续微调的小样本适配效果更优，可迁移到推荐系统新市场/新类目冷启动场景，用历史/合成数据做元预训练，少量新域数据即可快速适配

  - 不同架构适配增益差异大，落地小样本域适配方案时优先在Encoder类轻量模型上试点，投入产出比更高'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
语码转换（CS）ASR落地面临核心痛点：真实CS语音标注数据采集成本极高，低成本合成CS语音和真实语音分布存在显著gap，直接在合成数据上做持续微调易过拟合，泛化到真实场景效果差。
### 方法关键点
1. 基于Reptile元学习构建SyRA-CS合成到真实域适配框架，为每个语言对训练适配友好的初始化参数
2. 流水线为：先在对应语言对的合成CS-FLEURS子集完成元训练，再仅用1小时标注真实目标语音完成微调
3. 兼容Encoder-CTC、FastConformer-RNN-T、AED、Speech-LLM四类主流ASR架构
### 关键结果
在阿拉伯/法/德/印地语-英语4个语言对的16组模型-语言对对比实验中，WER全优于普通持续微调，CER在15组占优；XLS-R模型相对WER下降17.7%，其余三类模型相对WER下降5.3%~5.8%
