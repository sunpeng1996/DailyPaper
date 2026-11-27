---
title: 'ProxyGenBench: Benchmarking Proxy-Guided Video Generation'
title_zh: ProxyGenBench：代理引导视频生成评测基准
authors:
- Zhenchen Tang
- Haolin Lu
- Songlin Yang
- Xiaotong Zhao
- Ran Zhang
- Bo Peng
- Shuai Li
- Haotian Fan
- Haobin Zhong
- Yanni Zhang
affiliations:
- 中国科学院自动化研究所模式识别新实验室
- 加州大学圣地亚哥分校
- 香港科技大学
- 腾讯
- 中国科学院大学人工智能学院
arxiv_id: '2611.34457'
url: https://arxiv.org/abs/2611.34457
pdf_url: https://arxiv.org/pdf/2611.34457
published: '2026-11-24'
collected: '2026-11-27'
category: Eval
direction: 视频生成评测 · 代理引导可控生成
tags:
- Video Generation
- Benchmark
- Structural Proxy
- Multimodal Generation
- Evaluation
one_liner: 提出面向代理引导视频生成的三维度评测基准，覆盖3类任务共312个可控评测用例
practical_value: '- 做电商商品宣传视频、直播切片自动生成等可控生成业务时，可直接复用P（结构保留）/C（内容补全）/B（条件绑定）三维度评测框架，替代部分人工主观评测，提升评测效率

  - 做多条件引导生成任务（如文本+草稿生成商品短视频）时，可参考结论：无需盲目追求引导代理的细节度，过高的代理瑕疵反而会降低生成内容的补全质量

  - 做Agent驱动的内容生成链路时，可引入粗粒度结构代理作为中间控制层，平衡生成自由度和时空一致性，适配多镜头商品广告自动生成场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前视频生成模型写实性达标，但场景展开可控性不足；结构代理（如3D粗模）可指定布局、动作、相机路径、事件顺序，但存在细节缺失、自带瑕疵问题，现有评测体系未覆盖代理引导生成的特有需求。
### 方法关键点
构建含60个场景312个评测用例的基准，覆盖多镜头叙事、动态动作一致性、多视角一致性3类任务，设置代理保真度、文本细节、多模态输入三类控制变量，从结构保留（P）、内容补全（C）、条件绑定（B）三个维度做细粒度评测，额外提供综合三项维度的结构感知Strict得分。
### 关键结果数字
测试5款主流视频生成模型，结构代理平均提升时空控制效果12%以上，但代理细节度每提升20%，内容补全得分平均下降4.7%；结构贴合度高不代表多模态条件绑定正确率高，参与测试的最优模型Strict得分仅为45（满分100）。
