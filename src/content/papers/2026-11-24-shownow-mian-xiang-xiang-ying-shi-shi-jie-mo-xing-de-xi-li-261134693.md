---
title: 'ShowNow: Fine-Grained Speculative Streaming for Responsive World Models'
title_zh: ShowNow：面向响应式世界模型的细粒度推测流式框架
authors:
- Yiren Song
- Guian Fang
- Mike Zheng Shou
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2611.34693'
url: https://arxiv.org/abs/2611.34693
pdf_url: https://arxiv.org/pdf/2611.34693
published: '2026-11-24'
collected: '2026-11-27'
category: Multimodal
direction: 交互式世界模型 · 低延迟流式推理
tags:
- StreamingInference
- LowLatency
- WorldModel
- SpeculativeDecoding
- InteractiveSystem
one_liner: 提出细粒度推测流式框架ShowNow，大幅降低交互式世界模型的输入响应延迟
practical_value: '- 可复用「空闲计算期预生成多分支候选+用户输入后直接匹配」的思路，降低电商直播实时互动、智能导购Agent的响应延迟，优化用户交互体验

  - 共享历史树执行+融合提交的工程优化方法，可直接迁移到多候选生成类任务（如多query改写、多推荐文案生成），减少重复计算开销

  - 细粒度单潜变量提交的设计思路，可借鉴到生成式推荐的流式输出场景，平衡生成质量与响应速度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互式世界模型需连续生成视频并快速响应用户动作，现有方案仅优化吞吐量未解决输入延迟问题：粗粒度生成块会延迟动作更新，输入后再生成会拉长响应路径。
### 方法关键点
1. 利用播放空闲计算期预生成不同动作对应的未来分支结果，支持1-8个动作的可配置预生成；
2. 采用单潜变量提交实现高频决策，兼顾响应速度与生成粒度；
3. 构建多未来数据集训练同状态下的多分支延续，通过共享历史树执行、融合提交优化预生成效率。
### 关键结果
单H100上5B参数模型可实现8分支预生成下480p 16fps生成；ViZDoom场景下中位数输入到显示延迟从620ms降至208ms，重启空节拍从1.56%降至0.09%，按时响应率显著提升。
