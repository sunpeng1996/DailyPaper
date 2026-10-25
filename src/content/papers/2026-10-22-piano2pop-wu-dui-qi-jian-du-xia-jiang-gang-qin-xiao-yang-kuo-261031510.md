---
title: 'Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision'
title_zh: Piano2Pop：无对齐监督下将钢琴小样扩展为流行音乐成品
authors:
- Yun-Chen Cheng
- Chih-Pin Tan
- Tzu-Hung Huang
- Yi-Hsuan Yang
affiliations:
- National Taiwan University, Taiwan
arxiv_id: '2610.31510'
url: https://arxiv.org/abs/2610.31510
pdf_url: https://arxiv.org/pdf/2610.31510
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 音乐生成 · 无对齐监督跨域转换
tags:
- MusicGeneration
- PseudoSupervision
- FlowMatching
- DataAugmentation
one_liner: 提出无对齐监督的钢琴MIDI转流行器乐生成框架，基于伪监督训练预训练流匹配模型
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有研究多聚焦流行音乐转钢琴的降维任务，钢琴小样转完整流行成品的扩展任务缺乏对齐标注数据，零基准方案效果较差。
### 方法关键点
1. 提出伪监督训练范式，无需真实对齐的钢琴-流行标注对，基于从流行录音衍生的合成钢琴-器乐对训练预训练流匹配模型
2. 对比两类伪数据源方案：含函数选择性（FST）、音域密度（RDA）增强的无对转录方案，以及对监督钢琴覆盖生成器方案
### 关键结果数字
在476组真实钢琴覆盖/流行对测试集上，对监督方案取得最优Fréchet音频距离、伴奏提示遵循度与频谱形状指标；FST可缓解无对训练输出钢琴占比过高的问题；所有微调系统效果均显著优于零-shot基线
