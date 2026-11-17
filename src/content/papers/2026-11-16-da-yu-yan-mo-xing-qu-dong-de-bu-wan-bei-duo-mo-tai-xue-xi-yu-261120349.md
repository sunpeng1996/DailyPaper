---
title: Words Speak Louder? Exploring the Language Shortcut of LLM-Driven Incomplete
  Multimodal Learning
title_zh: 大语言模型驱动的不完备多模态学习语言捷径问题研究
authors:
- Wenhao Li
- Chong Xiao
- Xiaokun Bai
- Rundong He
- Zhuang Qi
- Xusheng Liang
- Zhibin Wu
- Qiangchang Wang
affiliations:
- Shandong University
- Shenzhen Loop Area Institute
- The Hong Kong Polytechnic University
- National University of Singapore
- City University of Hong Kong
arxiv_id: '2611.20349'
url: https://arxiv.org/abs/2611.20349
pdf_url: https://arxiv.org/pdf/2611.20349
published: '2026-11-16'
collected: '2026-11-17'
category: Multimodal
direction: 多模态LLM融合 语言捷径规避优化
tags:
- Multimodal-LLM
- Shortcut-Mitigation
- Multimodal-Fusion
- Benchmark
- Training-Method
one_liner: 提出CoVeR训练方法缓解多模态融合语言捷径，配套开源MR-Bench评测基准
practical_value: '- 电商多模态广告/商品内容理解场景可引入CoVeR训练逻辑，避免文本语义覆盖视觉/音频特征，提升短视频广告情绪识别、商品标签打标的准确率

  - 不完备多模态输入（缺音频/缺视频）的推荐召回场景，可复用反事实视图校验逻辑，判断融合结果是否过度依赖单模态特征，减少badcase

  - 多模态模型评测体系搭建可参考MR-Bench的构建思路，针对性构造单模态特征冲突的测试case，提前发现模型捷径问题'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前以LLM为融合引擎的不完备多模态学习方案普遍存在语言捷径问题：文本特征会覆盖视觉、音频等非语言模态的有效信号，导致多模态模型出现判断错误。
### 方法关键点
1. 构建MR-Bench评测集：包含MR-Bench-A（对4个情感基准的全量样本做类型标注）、MR-Bench-H（900条人工校验样本，含620条语言捷径、280条非语言捷径片段）
2. 提出反事实视图可靠性训练方法CoVeR：将各单模态视图作为独立判断器，单模态判断结果不一致时取消融合监督信号，推理无额外开销
### 关键结果
CoVeR在5个多模态基准上取得SOTA，在MR-Bench-H上语言捷径样本准确率达61.7%、非语言捷径样本准确率达93.6%；相比基线LLM-Fusion，加入文本后的错误率降低2.1个百分点
